"""R8: a dropdown filter drives its figure in the browser."""

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.e2e

YEAR_SELECTOR = "opt1-board1-menu-top-year"
GRAPH = "opt1-board1-graph-top"

# Airbnb & Homeaway average listings per location (bar heights), pinned from
# the current output for the default year and after adding 2016.
BARS_2015 = {"Chapinero": 232.5, "Usaquén": 93.5, "Candelaria": 37.125}
BARS_2015_2016 = {"Chapinero": 734.5, "Usaquén": 346.0, "Candelaria": 96.125}
LOCATIONS = 16


def _assert_bars(dash, expected):
    actual = dash.wait_for_bars(GRAPH, expected, LOCATIONS)
    assert len(actual) == LOCATIONS
    for location, value in expected.items():
        assert actual.get(location) == pytest.approx(value), location


def test_adding_a_year_updates_the_figure(dash):
    """R8: Given the accommodation page, when I add 2016, the bars are recomputed."""
    dash.open("/indicators/accomodation", "ACCOMMODATION")
    expect(dash.dropdown_values(YEAR_SELECTOR)).to_have_text(["2015"])
    _assert_bars(dash, BARS_2015)

    dash.dropdown_type(YEAR_SELECTOR, "2016")
    dash.page.keyboard.press("Enter")

    expect(dash.dropdown_values(YEAR_SELECTOR)).to_have_text(["2015", "2016"])
    _assert_bars(dash, BARS_2015_2016)
