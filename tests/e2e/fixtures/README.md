# Vendored e2e fixtures

The e2e suite runs with a hermetic network: the browser never reaches the
internet. Requests the app makes to third parties are answered from these
files (or with empty stubs, see `tests/e2e/conftest.py`), so rendering is the
same on every run and on every machine.

| File | Answers requests to | Source | Version | Licence | sha256 |
|---|---|---|---|---|---|
| `bootswatch-4.5.2-sandstone.min.css` | `stackpath.bootstrapcdn.com/bootswatch/4.5.2/sandstone/bootstrap.min.css` (`dbc.themes.SANDSTONE`) | that URL | Bootswatch 4.5.2 / Bootstrap 4.5.2 | MIT | `aa1eeeb3c81c755b701fd40d5f59ea0aaa49f71d3241dd12c462d64082759c21` |
| `world_110m.json` | `cdn.plot.ly/world_110m.json` (topojson for `scatter_geo`) | that URL | as served by cdn.plot.ly on 2026-11-15 | MIT (plotly.js) | `d75915eaa31c870df6b972c9e5bb86910197825f33dcfef740f3b2f68cffe843` |

Everything else external is answered with stubs: images (S3 assets, and Carto
basemap tiles, which mapbox-gl fetches from web workers) get a 1×1 PNG, and
fonts/CSS get empty responses. Hosts are allow-listed in `KNOWN_EXTERNAL_HOSTS`
(`tests/e2e/conftest.py`); a request to any other host fails the test.

Update the vendored files only together with the dependency that references them
(`dash-bootstrap-components` theme URL, plotly version).
