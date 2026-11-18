"""URL routing: pathname -> page."""

from dashboard.pages import about_us, home, indicators, travelers
from dashboard.shell import options_drop_navBar, options_navBar

NOT_FOUND = "ERROR 404: Page not found!"

_TRAVELERS = options_drop_navBar[options_navBar[1]]
_INDICATORS = options_drop_navBar[options_navBar[2]]

# Checked in order with str.endswith, as before.
ROUTES = [
    (_TRAVELERS[0]["value"], travelers.who),
    (_TRAVELERS[1]["value"], travelers.preferences),
    (_INDICATORS[0]["value"], indicators.accommodation),
    (_INDICATORS[1]["value"], indicators.connectivity),
    (_INDICATORS[2]["value"], indicators.economic),
    (_INDICATORS[3]["value"], indicators.sightseeing),
    ("/about-us", about_us.about_us),
]


def display_page(pathname):
    # Legacy quirk kept on purpose: `"/" or ""` is just "/", so an empty
    # pathname is a 404 (characterized in tests/test_pages.py).
    if pathname.endswith("/" or ""):
        return home.home()
    for suffix, page in ROUTES:
        if pathname.endswith(suffix):
            return page()
    return NOT_FOUND
