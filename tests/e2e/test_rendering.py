"""R1, R2, R9, R10: every page renders in a real browser."""

import pytest
from playwright.sync_api import expect

import app as legacy
from dash import dcc
from helpers import iter_components, page_layouts

pytestmark = pytest.mark.e2e

# Route -> positive readiness signal (text that only that page shows).
ROUTES = {
    "/": "Welcome",
    "/travelers/who": "THE TRAVELERS",
    "/travelers/preferences": "THE PREFERENCES",
    "/indicators/accomodation": "ACCOMMODATION",
    "/indicators/connectivity": "CONNECTIVITY",
    "/indicators/economic": "ECONOMIC",
    "/indicators/sightseeing": "SIGHTSEEING",
    "/about-us": "work team",
}

# How many dcc.Graph components each page declares. This is structure read
# from the layout, not computed behaviour.
GRAPH_COUNTS = {
    path: sum(isinstance(c, dcc.Graph) for c in iter_components(layout))
    for path, layout in page_layouts(legacy).items()
}

TEAM = [
    "Alberto Cortés",
    "Diego Cabrera",
    "Elizabeth Rendón",
    "Kelly García",
    "Paul Moros",
    "Sergio Rairán",
]


def test_every_route_is_covered():
    assert set(ROUTES) == set(GRAPH_COUNTS)


@pytest.mark.parametrize("path", list(ROUTES))
def test_route_renders(dash, path):
    """R1: Given the app runs, when I open a route, it renders completely."""
    dash.open(path, ROUTES[path])

    for shell_id in ("header-app", "navbar", "footer-app"):
        expect(dash.page.locator("#%s" % shell_id)).to_be_visible()
    expect(dash.page.locator("#page-content")).to_contain_text(ROUTES[path])

    expected_graphs = GRAPH_COUNTS[path]
    assert dash.graphs_with_data(expected_graphs) == expected_graphs


def test_unknown_route_shows_404_inside_shell(dash):
    """R2"""
    dash.open("/does-not-exist", "ERROR 404: Page not found!")
    expect(dash.page.locator("#navbar")).to_be_visible()
    expect(dash.page.locator("#footer-app")).to_be_visible()


def test_landing_page_content(dash):
    """R9"""
    dash.open("/", "Welcome")
    expect(dash.page.locator("#landing-title")).to_have_text(
        "Welcometo the Bogotá tourist information system"
    )


def test_about_us_lists_the_team(dash):
    """R9"""
    dash.open("/about-us", "work team")
    names = dash.page.locator("#page-content b")
    expect(names).to_have_count(len(TEAM))
    assert sorted(names.all_inner_texts()) == TEAM


def test_mobile_navbar_collapses_and_expands(mobile_dash):
    """R10: Given a phone-sized viewport, the navbar collapses behind a toggler."""
    mobile_dash.open("/", "Welcome")
    page = mobile_dash.page
    travelers = page.locator("#navbar").get_by_text("TRAVELERS", exact=True)

    toggler = page.locator("#navbar .navbar-toggler")
    expect(toggler).to_be_visible()
    expect(travelers).to_be_hidden()

    toggler.click()
    expect(travelers).to_be_visible()
