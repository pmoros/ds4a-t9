"""Behaviour of the datalayer package that the characterization snapshots
don't cover: configuration, validation, caching and the traveler-kind rule."""

import subprocess
import sys
import textwrap

import pandas as pd
import pytest

import datalayer
from datalayer import config, sources
from datalayer.schema import TravelerKind

# --------------------------------------------------------------------------
# AC7: national/international rule (the logic app.py copied 37 times)
# --------------------------------------------------------------------------


@pytest.mark.parametrize(
    "national, international, expected",
    [
        (0, 0, TravelerKind.NATIONAL),  # initial state: nothing clicked
        (1, 1, TravelerKind.NATIONAL),  # tie
        (2, 1, TravelerKind.NATIONAL),
        (1, 2, TravelerKind.INTERNATIONAL),
        ("1", "2", TravelerKind.INTERNATIONAL),  # Dash may send strings
        ("2", "1", TravelerKind.NATIONAL),
    ],
)
def test_kind_from_clicks(national, international, expected):
    assert datalayer.kind_from_clicks(national, international) is expected


def test_kind_from_clicks_rejects_missing_timestamps():
    with pytest.raises(TypeError):
        datalayer.kind_from_clicks(None, 0)


def test_traveler_kind_matches_source_values():
    assert TravelerKind.NATIONAL.value == "TURISTAS NACIONALES"
    assert TravelerKind.INTERNATIONAL.value == "TURISTAS INTERNACIONALES"


# --------------------------------------------------------------------------
# Travelers
# --------------------------------------------------------------------------


@pytest.mark.parametrize("kind", list(TravelerKind))
def test_travelers_by_kind_keeps_index_and_columns(kind):
    everyone = datalayer.travelers()
    subset = datalayer.travelers(kind)
    assert list(subset.columns) == list(everyone.columns)
    assert set(subset["TEMA"]) == {kind.value}
    pd.testing.assert_frame_equal(subset, everyone.loc[subset.index])


def test_options_keep_source_order():
    years = datalayer.options("AÑO")
    assert list(years) == list(pd.unique(datalayer.travelers()["AÑO"]))


@pytest.mark.parametrize(
    "label, expected",
    [("A. HOMBRE", "HOMBRE"), ("G. NS/NR", "NS/NR"), ("AB", "")],
)
def test_strip_prefix(label, expected):
    assert datalayer.strip_prefix(label) == expected


# --------------------------------------------------------------------------
# AC4: configuration by environment, clear errors
# --------------------------------------------------------------------------


def test_missing_data_dir_names_the_path(tmp_path, monkeypatch):
    monkeypatch.setenv("IDT_DATA_DIR", str(tmp_path))
    with pytest.raises(FileNotFoundError, match=str(tmp_path)):
        sources.load_travelers()


def test_missing_column_raises_schema_error(tmp_path, monkeypatch):
    csv = tmp_path / config.INDICATORS_FILE
    csv.write_text('"TEMA","SUBTEMA","AÑO","Valor"\n"x","y","2020","1"\n', encoding="utf-8")
    monkeypatch.setenv("IDT_DATA_DIR", str(tmp_path))
    with pytest.raises(sources.DataSchemaError) as info:
        sources.load_indicators()
    message = str(info.value)
    assert config.INDICATORS_FILE in message
    for column in ("VARIABLE", "CLASE", "FUENTE", "MES"):
        assert column in message


def test_indicator_columns_are_upper_cased():
    raw = datalayer.indicators_raw()
    assert list(raw.columns) == [
        "TEMA",
        "SUBTEMA",
        "VARIABLE",
        "CLASE",
        "FUENTE",
        "AÑO",
        "MES",
        "VALOR",
    ]


def test_geojson_path_is_configurable(tmp_path, monkeypatch):
    geojson = tmp_path / "shapes.geojson"
    geojson.write_text('{"type": "FeatureCollection", "features": []}', encoding="utf-8")
    monkeypatch.setenv("IDT_GEOJSON_PATH", str(geojson))
    assert sources.load_geojson() == {"type": "FeatureCollection", "features": []}


# --------------------------------------------------------------------------
# AC3 / AC6: independent of the working directory; lazy and cached
# --------------------------------------------------------------------------


def _run_python(code, cwd):
    result = subprocess.run(
        [sys.executable, "-c", textwrap.dedent(code)],
        cwd=str(cwd),
        env={"PYTHONPATH": str(config.REPO_ROOT), "PATH": ""},
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_loads_from_any_working_directory(tmp_path):
    out = _run_python(
        """
        import datalayer
        print(len(datalayer.travelers()), len(datalayer.indicators_raw()))
        print(len(datalayer.load_geojson()["features"]))
        """,
        cwd=tmp_path,
    )
    travelers, indicators, features = (int(n) for n in out.split())
    assert travelers > 0 and indicators > 0 and features > 0


def test_import_reads_nothing(tmp_path):
    out = _run_python(
        """
        import pandas as pd
        calls = []
        pd.read_csv = lambda *a, **k: calls.append("csv")
        pd.read_excel = lambda *a, **k: calls.append("excel")

        import datalayer
        from datalayer import indicators, sources
        sizes = [f.cache_info().currsize for f in sources.CACHED_READERS]
        sizes.append(indicators._build.cache_info().currsize)
        print(calls, sizes)
        """,
        cwd=tmp_path,
    )
    assert out.strip() == "[] [0, 0, 0, 0]"


def test_sources_are_read_once(monkeypatch):
    datalayer.clear_caches()
    reads = []
    real = pd.read_excel
    monkeypatch.setattr(pd, "read_excel", lambda *a, **k: reads.append(1) or real(*a, **k))
    first = sources.load_travelers()
    assert sources.load_travelers() is first
    assert reads == [1]


# --------------------------------------------------------------------------
# Indicator specs: edge cases the real data doesn't exercise
# --------------------------------------------------------------------------


def test_service_provider_split_excludes_exactly_400(tmp_path, monkeypatch):
    header = '"TEMA","SUBTEMA","VARIABLE","CLASE","Fuente","AÑO","Mes","Valor"\n'
    rows = "".join(
        '"Prestadores de Servicios Turísticos - PST","P%s","Total","","src","2020","","%s"\n'
        % (value, value)
        for value in (399, 400, 401)
    )
    (tmp_path / config.INDICATORS_FILE).write_text(header + rows, encoding="utf-8")
    monkeypatch.setenv("IDT_DATA_DIR", str(tmp_path))

    large = datalayer.indicator("prest_servicios_turisticos1")
    small = datalayer.indicator("prest_servicios_turisticos2")
    assert list(large["VALOR"]) == [401.0]
    assert list(small["VALOR"]) == [399.0]
