"""WSGI entry point: ``gunicorn -c gunicorn.conf.py app:server``."""

from dashboard import create_app
from dashboard.routes import display_page  # noqa: F401  (used by the tests)

app = create_app()
server = app.server

# Development server only; production runs gunicorn.
if __name__ == "__main__":
    import settings

    config = settings.load()
    app.run(debug=config.debug, host=config.host, port=config.port)
