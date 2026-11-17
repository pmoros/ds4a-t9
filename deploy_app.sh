#!/usr/bin/env bash
# Production server. Configure with PORT, WEB_CONCURRENCY and GUNICORN_THREADS
# (see gunicorn.conf.py).
set -euo pipefail
cd "$(dirname "$0")"
exec gunicorn -c gunicorn.conf.py app:server
