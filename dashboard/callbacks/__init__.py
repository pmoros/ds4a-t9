"""Callback registration, in the original order (routing, indicators, travelers)."""

from dash.dependencies import Input, Output

from dashboard import routes
from dashboard.callbacks import indicators, travelers


def register(app):
    app.callback(Output("page-content", "children"), [Input("url", "pathname")])(
        routes.display_page
    )
    indicators.register(app)
    travelers.register(app)
