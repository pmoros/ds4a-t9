# Dashboard IDT

## Introduction

This application has been developed using **Python**, mainly the **Dash Framework**. We suggest to deploy it in a **RHEL ** **based operating system**, however it is possible to deploy it using other O.S, this guide and the elements provided to make this process easier may not work that well.

## Running

The app is configured only through environment variables:

| Variable | Default | Used by | Purpose |
|---|---|---|---|
| `PORT` | `8050` | gunicorn, dev server | Port to listen on |
| `WEB_CONCURRENCY` | `2` | gunicorn | Worker processes |
| `GUNICORN_THREADS` | `4` | gunicorn | Threads per worker |
| `HOST` | `127.0.0.1` | dev server | Interface for `python app.py` (gunicorn always binds `0.0.0.0`) |
| `DASH_DEBUG` | `false` | dev server | Dash debug mode; never enable it on a reachable host |
| `IDT_DATA_DIR`, `IDT_GEOJSON_PATH` | repo files | app | Data location (see [Data layer](#data-layer)) |

### Docker

```bash
docker build -t ds4a-t9 .
docker run --rm -p 8050:8050 ds4a-t9            # http://localhost:8050
docker run --rm -e PORT=8080 -p 8080:8080 ds4a-t9
```

The image runs gunicorn as a non-root user and has a health check on `/`.

### Heroku-style platforms

`Procfile` runs `gunicorn -c gunicorn.conf.py app:server`, which binds the
`$PORT` the platform provides. `runtime.txt` pins Python 3.13.

### Locally

With [mise](https://mise.jdx.dev) (see [Development](#development)):

```bash
mise run serve        # Dash dev server with debug and reload, on 127.0.0.1:8050
mise run serve-prod   # gunicorn, exactly as in production
```

Without mise: `pip install -r requirements.txt`, then `./deploy_app.sh`.

## Development

Local tooling is managed by [mise](https://mise.jdx.dev) (`mise.toml`): it pins Python, [uv](https://docs.astral.sh/uv/), ruff and pre-commit, and defines the common tasks. CI uses the same file. Python dependencies live in `pyproject.toml` / `uv.lock`; `requirements.txt` (used by the Dockerfile and Procfile) is exported from the lock with `mise run export-requirements`.

```bash
mise install                  # Python 3.13, uv, ruff, pre-commit
mise run hooks                # install the git pre-commit hooks
mise run test                 # full suite: unit + characterization + e2e browser tests
mise run test-fast            # everything except the browser tests
mise run e2e                  # only the browser tests (installs Chromium on first run)
mise run test -- -k millify   # extra args go to pytest
mise run lint                 # ruff check + format check
mise run ci                   # everything CI runs
mise tasks                    # list all tasks
```

### Characterization tests

`tests/` freezes the current behaviour of the app before refactoring:

* `test_callbacks.py` runs all 54 Dash callbacks with first-load values, for national and international travelers, and snapshots their output (figures, card values, dropdown options, or the raised error).
* `test_pages.py` covers routing, page layouts and HTTP smoke tests.
* `test_data.py` profiles every DataFrame the data layer builds and snapshots the travelers/preferences cards.
* `test_charts.py` unit-tests the chart builders and filters on small synthetic frames.

### End-to-end tests

`tests/e2e/` drives the real app in headless Chromium (Playwright) to check that every page renders, navigation works, and the main cards, toggles and filters behave as expected. The app is served in-process, and the browser's network is hermetic: third-party requests (S3 images, CDN CSS, map tiles and topojson) are answered from `tests/e2e/fixtures/` or with stubs, so runs are deterministic and offline. Any page error, console error or failed callback fails the test. On failure, screenshots and Playwright traces are written to `test-results/` (open a trace with `uv run playwright show-trace <file>`).

Snapshots live in `tests/__snapshots__/`. If a change in output is **intended**, regenerate them with `mise run snapshot-update` and review the diff.

### Code layout

```
app.py              WSGI entry point: app = create_app(); server = app.server
dashboard/
  __init__.py       create_app(warm=True)
  shell.py          header, navbar, footer, page container
  routes.py         pathname -> page
  pages/            one module per section; pages are built on first use and cached
  callbacks/        callbacks declared as tables, registered in order
  charts.py         figure builders and the frame filters behind them
  components.py     shared UI pieces (banners, board headers, dropdown options)
  theme.py          colours, palettes, month order
datalayer/          all data access (below)
```

`create_app()` builds every page at startup, so a bad data directory fails
before gunicorn forks its workers. `create_app(warm=False)` defers all reads
until a page is requested.

### Data layer

All data access goes through the `datalayer` package. Callbacks and layouts
never read files or raw columns themselves; `tests/test_boundaries.py`
enforces that.

| Variable | Default | Purpose |
|---|---|---|
| `IDT_DATA_DIR` | `<repo>/data` | Folder with `base_viajeros.xlsx` and the indicators CSV |
| `IDT_GEOJSON_PATH` | `<repo>/assets/colombia.geojson` | Department shapes for the national map |

Sources are read on first use and cached. A missing file or column fails with
an error naming the file. New indicators are added as an `IndicatorSpec` in
`datalayer/indicators.py`.

## Authors

### DS4A Cohort 5 - Team 9

* Alberto Cortes
* Elizabeth Rendon
* Kelly Garcia
* Paul Moros
* Sergio Rairan
* Diego Cabrera



