"""The IDT tourism dashboard as a package. ``create_app()`` is the entry point."""

from pathlib import Path

import dash
import dash_bootstrap_components as dbc

from dashboard import callbacks, pages, shell

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"


def create_app(warm=True):
    """Build the Dash app.

    With ``warm`` (the default, used by app.py) every page is built right away,
    so a missing or invalid data directory fails at startup, before gunicorn
    forks its workers. With ``warm=False`` nothing is read until a page is
    requested.
    """
    app = dash.Dash(
        "app",
        assets_folder=str(ASSETS_DIR),
        # Dash 1.x compressed responses by default; Dash 2 needs it asked for.
        compress=True,
        external_stylesheets=[dbc.themes.SANDSTONE],
        meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    )
    app.title = "IDT Dashboard"
    app.config.suppress_callback_exceptions = True
    app.layout = shell.layout()
    callbacks.register(app)
    if warm:
        pages.warm()
    return app
