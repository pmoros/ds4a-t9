"""Harness for the end-to-end browser tests.

* The real Dash app is served in-process by a threaded Werkzeug server on a
  free localhost port (``base_url`` overrides pytest-base-url's fixture, so
  ``page.goto("/travelers/who")`` works).
* The network is hermetic. Requests to localhost pass through. Every
  third-party request is answered from a vendored fixture or an empty stub,
  never aborted, so the console stays clean and runs are reproducible
  (see fixtures/README.md).
* ``dash`` wraps the Playwright page. It fails the test on any page error,
  console error, or failed Dash callback request, and it knows how to wait
  until Dash has finished updating.
"""

import base64
import json
import logging
import threading
from pathlib import Path
from urllib.parse import urlparse

import pytest

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import expect
from werkzeug.serving import make_server

FIXTURES = Path(__file__).parent / "fixtures"
EMPTY_MAP_STYLE = json.dumps({"version": 8, "sources": {}, "layers": []})
APP_TITLE = "IDT Dashboard"
UPDATE_PATH = "/_dash-update-component"
LOCAL_HOSTS = {"127.0.0.1", "localhost"}

# Every third-party host the app is known to contact (all answered by stubs).
# A request to any other host fails the test, so a new external dependency
# gets noticed instead of being stubbed silently.
KNOWN_EXTERNAL_HOSTS = (
    "ds4a-team9-idt.s3.us-east-2.amazonaws.com",  # images
    "cdn.jsdelivr.net",  # Bootswatch theme (vendored)
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "static.wixstatic.com",
    "cdn.plot.ly",  # geo topojson (vendored)
    "basemaps.cartocdn.com",  # Carto MapLibre style (stubbed with an empty style)
)


def _is_known_external(host):
    return any(
        host == known or (known.startswith(".") and host.endswith(known))
        for known in KNOWN_EXTERNAL_HOSTS
    )


DESKTOP = {"width": 1280, "height": 900}
MOBILE = {"width": 375, "height": 812}

# Smallest valid PNG (1x1, transparent), used for every remote image.
PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
)
IMAGE_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".webp")

STUB_CONTENT_TYPES = {
    "stylesheet": "text/css",
    "script": "application/javascript",
    "font": "font/woff2",
    "fetch": "application/json",
    "xhr": "application/json",
}

# Counts Dash callback requests that are still in flight. Dash's
# renderer uses window.fetch for /_dash-update-component.
TRACK_DASH_REQUESTS = (
    """
(() => {
  window.__dashPending = 0;
  const origFetch = window.fetch.bind(window);
  window.fetch = (...args) => {
    const url = String(args[0] && args[0].url ? args[0].url : args[0]);
    if (!url.includes('%s')) return origFetch(...args);
    window.__dashPending += 1;
    return origFetch(...args).finally(() => { window.__dashPending -= 1; });
  };
})();
"""
    % UPDATE_PATH
)

DASH_IDLE = "() => window.__dashPending === 0 && document.title === %s" % json.dumps(APP_TITLE)

COUNT_GRAPHS_WITH_DATA = """
() => Array.from(document.querySelectorAll('#page-content .js-plotly-plot'))
           .filter(gd => Array.isArray(gd.data) && gd.data.length > 0).length
"""


# --------------------------------------------------------------------------
# Server
# --------------------------------------------------------------------------


@pytest.fixture(scope="session")
def live_server(legacy_app):
    logging.getLogger("werkzeug").setLevel(logging.WARNING)  # no per-request noise
    server = make_server("127.0.0.1", 0, legacy_app.server, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield "http://127.0.0.1:%d" % server.server_port
    server.shutdown()
    thread.join(timeout=5)


@pytest.fixture(scope="session")
def base_url(live_server):
    return live_server


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    return {
        **browser_context_args,
        "base_url": base_url,
        "viewport": DESKTOP,
        "locale": "en-US",
        "timezone_id": "UTC",
        "reduced_motion": "reduce",
        "color_scheme": "light",
    }


# --------------------------------------------------------------------------
# Hermetic network
# --------------------------------------------------------------------------


def _fulfill_external(route, stubbed):
    request = route.request
    url = request.url
    parsed = urlparse(url)
    stubbed.append(url)

    if "bootswatch@5.3.6/dist/sandstone" in url:
        route.fulfill(path=FIXTURES / "bootswatch-5.3.6-sandstone.min.css")
    elif parsed.path.endswith("/style.json"):
        # MapLibre basemap style (Carto). An empty style draws no basemap and
        # requests no tiles, sprites or fonts; the choropleth still renders.
        route.fulfill(body=EMPTY_MAP_STYLE, content_type="application/json")
    elif parsed.hostname == "cdn.plot.ly" and parsed.path.endswith(".json"):
        route.fulfill(path=FIXTURES / "world_110m.json")
    elif request.resource_type == "image" or parsed.path.lower().endswith(IMAGE_SUFFIXES):
        route.fulfill(body=PNG_1X1, content_type="image/png")
    else:
        content_type = STUB_CONTENT_TYPES.get(request.resource_type, "text/plain")
        route.fulfill(status=200, body="", content_type=content_type)


def install_hermetic_network(context):
    """Route every request; returns the list of stubbed third-party URLs."""
    stubbed = []

    def handler(route):
        if urlparse(route.request.url).hostname in LOCAL_HOSTS:
            route.continue_()
        else:
            _fulfill_external(route, stubbed)

    context.route("**/*", handler)
    context.add_init_script(TRACK_DASH_REQUESTS)
    return stubbed


# --------------------------------------------------------------------------
# Dash page helper
# --------------------------------------------------------------------------


class DashPage:
    def __init__(self, page):
        self.page = page
        self.errors = []
        self.stubbed = install_hermetic_network(page.context)
        page.set_default_timeout(20_000)
        page.on("pageerror", lambda exc: self.errors.append("pageerror: %s" % exc))
        page.on("console", self._on_console)
        page.on("response", self._on_response)

    def _on_console(self, message):
        if message.type == "error":
            self.errors.append("console: %s" % message.text)

    def _on_response(self, response):
        if UPDATE_PATH in response.url and response.status >= 400:
            self.errors.append("callback HTTP %d: %s" % (response.status, response.url))

    # -- navigation / waiting ------------------------------------------------

    def open(self, path, ready_text):
        """Go to ``path``, wait for a route-specific signal, then for Dash idle."""
        self.page.goto(path)
        expect(self.page.locator("#page-content")).to_contain_text(ready_text)
        self.wait_idle()

    def wait_idle(self):
        self.page.wait_for_function(DASH_IDLE)

    def graphs_with_data(self, expected):
        """Wait until ``expected`` graphs have traces; return the final count."""
        try:
            self.page.wait_for_function(
                "n => (%s)() === n" % COUNT_GRAPHS_WITH_DATA.strip(), arg=expected
            )
        except PlaywrightError:
            pass  # fall through to report the actual count
        return self.page.evaluate(COUNT_GRAPHS_WITH_DATA)

    # -- dcc.Dropdown helpers (Dash 4) ---------------------------------------
    # The open menu is rendered in a popover at the end of <body>, outside the
    # component's own element; only one is open at a time.

    def dropdown(self, component_id):
        return self.page.locator("#%s" % component_id)

    def dropdown_values(self, component_id):
        return self.dropdown(component_id).locator(".dash-dropdown-value-item")

    def dropdown_menu(self):
        return self.page.locator(".dash-dropdown-content")

    def dropdown_type(self, component_id, text):
        self.dropdown(component_id).locator(".dash-dropdown-trigger").click()
        self.dropdown_menu().locator("input.dash-dropdown-search").fill(text)

    def wait_for_bars(self, graph_id, expected, traces):
        """Poll until a bar figure has ``traces`` traces and the ``expected``
        {trace name: first y} values; return what is rendered at the end.

        Polling (rather than reading once after wait_idle) avoids racing
        Plotly's re-render after the callback response arrives. Values are read
        from ``_fullData``: plotly >= 6 sends arrays base64-encoded, and only
        the computed traces hold them decoded.
        """
        try:
            self.page.wait_for_function(
                """([id, expected, traces]) => {
                     const gd = document.querySelector('#' + id + ' .js-plotly-plot');
                     if (!gd || !Array.isArray(gd.data) || gd.data.length !== traces) return false;
                     const bars = Object.fromEntries(gd._fullData.map(t => [t.name, Number(t.y[0])]));
                     return Object.entries(expected).every(
                       ([name, v]) => name in bars && Math.abs(bars[name] - v) <= 1e-6 * Math.max(1, Math.abs(v)));
                   }""",
                arg=[graph_id, expected, traces],
            )
        except PlaywrightError:
            pass  # fall through so the caller's assertion shows the actual values
        return self.page.evaluate(
            """id => {
                 const gd = document.querySelector('#' + id + ' .js-plotly-plot');
                 if (!gd || !Array.isArray(gd.data)) return {};
                 return Object.fromEntries(gd._fullData.map(t => [t.name, Number(t.y[0])]));
               }""",
            graph_id,
        )

    # -- teardown checks -----------------------------------------------------

    def settle(self):
        """Let in-flight callbacks finish so late failures are still caught."""
        try:
            self.wait_idle()
        except PlaywrightError as exc:
            self.errors.append("app did not settle: %s" % exc)

    def unknown_hosts(self):
        hosts = {urlparse(url).hostname or url for url in self.stubbed}
        return sorted(h for h in hosts if not _is_known_external(h))


def _assert_clean(dash_page):
    assert dash_page.errors == [], "browser errors:\n" + "\n".join(dash_page.errors)
    assert dash_page.unknown_hosts() == [], (
        "the app contacted new third-party hosts; stub them and add them to " "KNOWN_EXTERNAL_HOSTS"
    )


@pytest.fixture
def dash(page):
    dash_page = DashPage(page)
    yield dash_page
    dash_page.settle()
    _assert_clean(dash_page)


@pytest.fixture
def mobile_dash(browser, browser_context_args):
    context = browser.new_context(**{**browser_context_args, "viewport": MOBILE})
    dash_page = DashPage(context.new_page())
    yield dash_page
    dash_page.settle()
    context.close()
    _assert_clean(dash_page)
