"""The dashboard package: app factory, assets, lazy pages, boot-time failure."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
CALLBACK_KEYS = (REPO_ROOT / "tests" / "callback_keys.txt").read_text().split()
STYLESHEETS = sorted(p.name for p in (REPO_ROOT / "assets").glob("style-*.css"))


def test_callbacks_registered_in_the_original_order(legacy_app):
    assert list(legacy_app.app.callback_map) == CALLBACK_KEYS


@pytest.mark.parametrize("stylesheet", STYLESHEETS)
def test_assets_are_served_and_linked(client, stylesheet):
    assert client.get("/assets/" + stylesheet).status_code == 200
    assert ("/assets/" + stylesheet).encode() in client.get("/").data


def test_index_html_keeps_theme_meta_and_title(client):
    html = client.get("/").data.decode()
    assert "bootswatch" in html and "sandstone" in html
    assert 'name="viewport"' in html and "width=device-width, initial-scale=1" in html
    assert "<title>IDT Dashboard</title>" in html


def test_assets_folder_is_the_repo_assets_dir(legacy_app):
    assert legacy_app.app.config.assets_folder == str(REPO_ROOT / "assets")


def test_pages_are_built_once_and_reused(legacy_app):
    from dashboard import routes

    for path in ["/", "/travelers/who", "/indicators/economic", "/about-us"]:
        assert routes.display_page(path) is routes.display_page(path)


def test_app_keeps_dash_settings(legacy_app):
    assert legacy_app.app.config.suppress_callback_exceptions is True
    assert legacy_app.app.title == "IDT Dashboard"


def _python(code, **env):
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=str(REPO_ROOT),
        env=dict(os.environ, **env),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        timeout=300,
    )


# Records every data source opened, by file name.
_TRACE = """
import builtins, io, sys
import pandas
opened = []
def spy(original):
    def wrapper(path, *args, **kwargs):
        opened.append(str(path).replace("\\\\", "/").rsplit("/", 1)[-1])
        return original(path, *args, **kwargs)
    return wrapper
pandas.read_excel = spy(pandas.read_excel)
pandas.read_csv = spy(pandas.read_csv)
builtins.open = spy(builtins.open)
"""


def test_create_app_without_warm_builds_nothing():
    result = _python(
        _TRACE
        + """
import dashboard
app = dashboard.create_app(warm=False)
data = sorted({name for name in opened if name.endswith((".xlsx", ".csv", ".geojson"))})
print("OPENED", data)
"""
    )
    assert result.returncode == 0, result.stdout
    assert "OPENED []" in result.stdout


def test_a_travelers_page_reads_only_the_travelers_source():
    result = _python(
        _TRACE
        + """
import dashboard
from dashboard import routes
app = dashboard.create_app(warm=False)
routes.display_page("/travelers/who")
data = sorted({name for name in opened if name.endswith((".xlsx", ".csv", ".geojson"))})
print("OPENED", data)
"""
    )
    assert result.returncode == 0, result.stdout
    assert "OPENED ['base_viajeros.xlsx']" in result.stdout


def test_importing_app_fails_fast_on_a_bad_data_dir():
    result = _python("import app", IDT_DATA_DIR="/nonexistent-idt-data")
    assert result.returncode != 0
    assert "FileNotFoundError" in result.stdout and "/nonexistent-idt-data" in result.stdout


def test_app_module_is_thin():
    lines = (REPO_ROOT / "app.py").read_text(encoding="utf-8").splitlines()
    assert len(lines) < 40


LEGACY_MODULES = ["index.py", "layouts.py", "layouts_viajeros.py"]
LEGACY_MODULES += ["layouts_indicators.py", "layouts_about_us.py"]


@pytest.mark.parametrize("module", LEGACY_MODULES)
def test_legacy_ui_modules_are_gone(module):
    assert not (REPO_ROOT / module).exists()


def test_no_wildcard_imports():
    sources = [REPO_ROOT / "app.py", *sorted((REPO_ROOT / "dashboard").rglob("*.py"))]
    offenders = [str(p) for p in sources if "import *" in p.read_text(encoding="utf-8")]
    assert offenders == []
