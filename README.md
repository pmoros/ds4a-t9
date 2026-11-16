# Dashboard IDT

## Introduction

This application has been developed using **Python**, mainly the **Dash Framework**. We suggest to deploy it in a **RHEL ** **based operating system**, however it is possible to deploy it using other O.S, this guide and the elements provided to make this process easier may not work that well.

## Setup

We provided a nice **bash** script to initialize the *production environment* for the application, this file is *setup* and in order to run it use the code below.

```bash
# Move to the project's folder
cd DS4A-T9 # You need to place your path

# Give execution permission
chmod +x setup

# Run the script
./setup
```

Once you have done this, it's pretty important that before launching the application you launch the *virtual environment* using `source venv/bin/activate`, otherwise the application will not find the required dependencies.

## Running

### Manual deployment

Now that you have already set up the environment for the application to run properly, we provided a script *deploy_app*, just run `./deploy_app.sh` and it will launch instantly.

### Cloud based assistant

The application has a *Procfile* that defines properties that tools used by cloud providers can easily use to launch the application. With that said, below you can find how to deploy the application using different providers.

* [Heroku](https://dash.plotly.com/deployment)
  * Be aware to initialize a complete new repository when using this alternative
* [AWS](https://austinlasseter.medium.com/deploying-a-dash-app-with-elastic-beanstalk-console-27a834ebe91d)
  * *You might have to meet costs.*

## Development

Local tooling is managed by [mise](https://mise.jdx.dev) (`mise.toml`): it pins Python, [uv](https://docs.astral.sh/uv/), ruff and pre-commit, and defines the common tasks. CI uses the same file. Python dependencies live in `pyproject.toml` / `uv.lock`, mirroring `requirements.txt` (still used by the Dockerfile and Procfile).

```bash
mise install                  # Python 3.8, uv, ruff, pre-commit
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
* `test_data.py` profiles every DataFrame built in `data.py` and snapshots the travelers/preferences cards.

### End-to-end tests

`tests/e2e/` drives the real app in headless Chromium (Playwright) to check that every page renders, navigation works, and the main cards, toggles and filters behave as expected. The app is served in-process, and the browser's network is hermetic: third-party requests (S3 images, CDN CSS, map tiles and topojson) are answered from `tests/e2e/fixtures/` or with stubs, so runs are deterministic and offline. Any page error, console error or failed callback fails the test. On failure, screenshots and Playwright traces are written to `test-results/` (open a trace with `uv run playwright show-trace <file>`).

Snapshots live in `tests/__snapshots__/`. If a change in output is **intended**, regenerate them with `mise run snapshot-update` and review the diff.

## Authors

### DS4A Cohort 5 - Team 9

* Alberto Cortes
* Elizabeth Rendon
* Kelly Garcia
* Paul Moros
* Sergio Rairan
* Diego Cabrera



