# Vendored e2e fixtures

The e2e suite runs with a hermetic network: the browser never reaches the
internet. Requests the app makes to third parties are answered from these
files (or with empty stubs, see `tests/e2e/conftest.py`), so rendering is the
same on every run and on every machine.

| File | Answers requests to | Source | Version | Licence | sha256 |
|---|---|---|---|---|---|
| `bootswatch-5.3.6-sandstone.min.css` | `cdn.jsdelivr.net/npm/bootswatch@5.3.6/dist/sandstone/bootstrap.min.css` (`dbc.themes.SANDSTONE`) | that URL | Bootswatch 5.3.6 / Bootstrap 5.3 | MIT | `2d7cd54bac13f87b4c8446d6da9468e82067568be598d0752c42908ed7f5daf4` |
| `world_110m.json` | `cdn.plot.ly/world_110m.json` (topojson for `scatter_geo`) | that URL | as served by cdn.plot.ly on 2026-11-15 | MIT (plotly.js) | `d75915eaa31c870df6b972c9e5bb86910197825f33dcfef740f3b2f68cffe843` |

Everything else external is answered with stubs: the Carto MapLibre basemap
style gets an empty style (so no tiles, sprites or fonts are requested), images
(S3 assets) get a 1×1 PNG, and
fonts/CSS get empty responses. Hosts are allow-listed in `KNOWN_EXTERNAL_HOSTS`
(`tests/e2e/conftest.py`); a request to any other host fails the test.

Update the vendored files only together with the dependency that references them
(`dash-bootstrap-components` theme URL, plotly version).
