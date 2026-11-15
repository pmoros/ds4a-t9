"""Characterization tests for the data layer (wrangler.py + data.py)."""

import pandas as pd
import pytest

import data
import layouts
import wrangler

DATAFRAME_NAMES = sorted(
    name for name, value in vars(data).items() if isinstance(value, pd.DataFrame)
)


def _profile(df):
    numeric = df.select_dtypes("number")
    return {
        "shape": list(df.shape),
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "numeric_sums": {col: round(float(numeric[col].sum()), 6) for col in numeric},
        "content_hash": str(pd.util.hash_pandas_object(df, index=True).sum()),
    }


def test_expected_dataframes_exist():
    assert "df_viajeros" in DATAFRAME_NAMES
    assert "df_indicadores_turismo" in DATAFRAME_NAMES


@pytest.mark.parametrize("name", DATAFRAME_NAMES)
def test_dataframe_profile(name, snapshot_json):
    assert _profile(getattr(data, name)) == snapshot_json


def test_wrangler_returns_both_databases():
    databases = wrangler.read__file_databases()
    assert set(databases) == set(wrangler.DATABASE_NAMES)
    assert all(col == col.upper() for col in databases["base_indicadores"].columns)


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, "0"),
        (999, "999"),
        (1500, "2 K"),
        (2500, "2 K"),  # str.format rounds half to even
        (1_234_567, "1 M"),
        (3_400_000_000, "3 B"),
        (-2500, "-2 K"),
    ],
)
def test_millify(value, expected):
    assert data.millify(value) == expected


def test_create_options_dropdown():
    assert layouts.create_options_dropdown(2021) == {"label": "2021", "value": "2021"}


def _card_cases():
    # Same defaults the app offers: years/months in order of appearance in the data.
    df = data.df_viajeros
    years = [int(y) for y in df["AÑO"].unique()[:2]]
    months = [m for m in df["MES"].unique() if m != "TOTAL"][:2]
    return [
        pytest.param(year, month, flag, id="%s-%s-flag%d" % (year, month, flag))
        for year in years
        for month in months
        for flag in (0, 1, 2)  # 0: international, 1: national, other: both
    ]


def _call_card(fn, *args):
    try:
        return fn(data.df_viajeros, *args)
    except Exception as exc:
        return {"error": type(exc).__name__, "message": str(exc)}


@pytest.mark.parametrize("year, month, flag", _card_cases())
def test_travel_card(year, month, flag, snapshot_json):
    assert _call_card(data.travelCard, year, month, flag) == snapshot_json


@pytest.mark.parametrize("year, month, flag", _card_cases())
def test_pref_card(year, month, flag, snapshot_json):
    assert _call_card(data.prefCard, year, month, flag) == snapshot_json
