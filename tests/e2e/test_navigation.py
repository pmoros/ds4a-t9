"""R3, R4: client-side navigation through the navbar."""

import re

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.e2e


def _open_menu_item(page, menu, item):
    page.locator("#navbar .dropdown-toggle", has_text=menu).click()
    page.locator("#navbar .dropdown-menu").get_by_text(item, exact=True).click()


def test_navbar_navigates_without_full_reload(dash):
    """R3: Given I'm on the home page, when I pick a navbar entry, the page swaps in place."""
    dash.open("/", "Welcome")
    dash.page.evaluate("window.__e2eMarker = 'still-here'")

    _open_menu_item(dash.page, "TRAVELERS", "Who are the travelers?")

    expect(dash.page).to_have_url(re.compile(r"/travelers/who$"))
    expect(dash.page.locator("#page-content")).to_contain_text("THE TRAVELERS")
    assert dash.page.evaluate("window.__e2eMarker") == "still-here"
    dash.wait_idle()


def test_nested_navigation_uses_relative_hrefs(dash):
    """R4 (characterization): navbar hrefs are relative, so links stack paths.

    From /travelers/who the preferences link resolves to
    /travelers/travelers/preferences. It still renders only because the router
    matches with ``endswith``. Fixing the hrefs will (correctly) fail this test.
    """
    dash.open("/travelers/who", "THE TRAVELERS")

    _open_menu_item(dash.page, "TRAVELERS", "What are their preferences?")

    expect(dash.page).to_have_url(re.compile(r"/travelers/travelers/preferences$"))
    expect(dash.page.locator("#page-content")).to_contain_text("THE PREFERENCES")
    dash.wait_idle()
