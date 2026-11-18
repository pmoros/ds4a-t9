"""R5, R6, R7: travelers pages, main cards and the traveler-type toggle.

Expected values are literals (the ones pinned by the characterization
snapshots), so a regression in the data layer fails here too. It does not move the
expectation along with it.
"""

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.e2e

TRAVEL_CARD_IDS = [
    "main-board-content-cantidad",
    "main-board-content-genero-hombre",
    "main-board-content-genero-mujer",
    "main-board-content-origin",
    "main-board-content-education",
    "main-board-content-age",
]
NATIONAL_CARD = ["37 M", "35%", "65%", "BOLIVAR", "PROFESIONAL UNIVERSITARIO", "DE 31 A 45"]
INTERNATIONAL_CARD = [
    "3 M",
    "61%",
    "39%",
    "ESTADOS UNIDOS",
    "PROFESIONAL UNIVERSITARIO",
    "DE 31 A 45",
]

PREF_CARD_IDS = [
    "main-board-content-purpose-0",
    "main-board-content-purpose-1",
    "most-visited-content-0",
    "most-visited-content-1",
    "main-board-content-travelgroup",
    "main-board-content-accomodation",
    "main-board-content-expense",
]
PREF_CARD = ["27%", "OTRO", "44%", "OTRO", "OTRO", "CASA PROPIA, DE FAMILIARES O AMIGOS", "OTRO"]

ORIGIN_SELECTOR = "travelers_opt1-board2-bottom-origin"


def _expect_card(page, ids, values):
    for component_id, value in zip(ids, values, strict=False):
        expect(page.locator("#%s" % component_id)).to_have_text(value)


def test_travelers_main_card_national_by_default(dash):
    """R5"""
    dash.open("/travelers/who", "THE TRAVELERS")
    expect(dash.dropdown_values("main-board-menu-year")).to_have_text(["2019"])
    expect(dash.dropdown_values("main-board-menu-month")).to_have_text(["ENERO"])
    _expect_card(dash.page, TRAVEL_CARD_IDS, NATIONAL_CARD)
    expect(dash.dropdown_values(ORIGIN_SELECTOR)).to_have_text(["ANTIOQUIA"])


def test_switching_to_international_travelers(dash):
    """R6: When I click "International travelers", cards and selectors update."""
    dash.open("/travelers/who", "THE TRAVELERS")
    _expect_card(dash.page, TRAVEL_CARD_IDS, NATIONAL_CARD)

    dash.page.locator("#viajeros-selector-international").click()

    _expect_card(dash.page, TRAVEL_CARD_IDS, INTERNATIONAL_CARD)
    expect(dash.dropdown_values(ORIGIN_SELECTOR)).to_have_text(["ALEMANIA"])

    # The options list is virtualized, so search instead of scanning it.
    dash.dropdown_type(ORIGIN_SELECTOR, "ESTADOS")
    expect(dash.dropdown_menu()).to_contain_text("ESTADOS UNIDOS")
    dash.page.keyboard.press("Escape")
    dash.wait_idle()


def test_preferences_main_card(dash):
    """R7"""
    dash.open("/travelers/preferences", "THE PREFERENCES")
    _expect_card(dash.page, PREF_CARD_IDS, PREF_CARD)


def test_month_selector_cannot_be_cleared(dash):
    """Clearing the month used to send None and answer HTTP 500."""
    dash.open("/travelers/who", "THE TRAVELERS")
    expect(dash.dropdown_values("main-board-menu-month")).to_have_text(["ENERO"])
    expect(dash.dropdown("main-board-menu-month").locator(".dash-dropdown-clear")).to_have_count(0)
    expect(dash.dropdown("main-board-menu-year").locator(".dash-dropdown-clear")).to_have_count(0)
