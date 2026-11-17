FROM python:3.7.11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PORT=8050

WORKDIR /app

# Dependencies first, so this layer is cached until requirements.txt changes.
COPY requirements.txt .
RUN pip install -r requirements.txt && pip check

RUN useradd --create-home --uid 10001 app
COPY --chown=app:app . .
USER app

EXPOSE 8050

# Data loads at boot, so give the app time before the first check.
HEALTHCHECK --interval=30s --timeout=10s --start-period=90s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:%s/' % os.environ.get('PORT', '8050'), timeout=5)"

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:server"]
