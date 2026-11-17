"""Gunicorn settings for production (12-factor: everything from the environment).

    PORT              port to bind on all interfaces (default 8050)
    WEB_CONCURRENCY   worker processes (default 2)
    GUNICORN_THREADS  threads per worker (default 4)

Run with:  gunicorn -c gunicorn.conf.py app:server
"""

import os

import settings

bind = ["0.0.0.0:%d" % settings.port_from(os.environ)]
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
threads = int(os.environ.get("GUNICORN_THREADS", "4"))

# The app loads its data at import. Preloading does that once, before the
# workers fork, so a missing or invalid data directory fails at boot instead
# of on the first request. (Not compatible with --reload; use `mise run serve`
# for development.)
preload_app = True

# First renders of the heavier figures can take a while.
timeout = 120
graceful_timeout = 30

# Logs go to stdout/stderr for the platform to collect.
accesslog = "-"
errorlog = "-"
