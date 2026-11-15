"""Routing, page layouts and HTTP smoke tests."""

import pytest

from helpers import PAGE_PATHS, display_page, iter_components, page_layouts, slug, to_jsonable

NOT_FOUND = "ERROR 404: Page not found!"


@pytest.mark.parametrize("path", PAGE_PATHS)
def test_route_resolves(legacy_app, path):
    assert display_page(legacy_app, path) != NOT_FOUND


def test_unknown_route_returns_404_text(legacy_app):
    assert display_page(legacy_app, "/does-not-exist") == NOT_FOUND


def test_empty_pathname_is_not_home(legacy_app):
    # Characterizes a known bug: `pathname.endswith("/" or "")` only checks "/",
    # so an empty pathname falls through to the 404 text.
    assert display_page(legacy_app, "") == NOT_FOUND


@pytest.mark.parametrize("path", PAGE_PATHS, ids=[slug(p) or "home" for p in PAGE_PATHS])
def test_page_layout(legacy_app, path, snapshot_json):
    assert to_jsonable(page_layouts(legacy_app)[path]) == snapshot_json


def test_component_ids_are_unique_per_page(legacy_app):
    for path, layout in page_layouts(legacy_app).items():
        ids = [c.id for c in iter_components(layout) if getattr(c, "id", None)]
        duplicates = sorted({i for i in ids if ids.count(i) > 1})
        assert duplicates == [], path


def test_app_shell_layout(legacy_app, snapshot_json):
    assert to_jsonable(legacy_app.app.layout) == snapshot_json


@pytest.mark.parametrize("path", PAGE_PATHS)
def test_http_page_served(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert b"IDT Dashboard" in response.data


def test_http_dash_layout(client):
    assert client.get("/_dash-layout").status_code == 200


def test_http_dash_dependencies(client):
    response = client.get("/_dash-dependencies")
    assert response.status_code == 200
    assert len(response.get_json()) == 54
