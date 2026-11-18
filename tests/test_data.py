"""Characterization tests for the data layer.

The snapshot ids are the legacy ``data.df_*`` names, so these tests prove the
datalayer reproduces every frame data.py used to build.
"""

import pandas as pd
import pytest

import datalayer
from datalayer import TravelerKind
from dashboard.components import create_options_dropdown
from datalayer.formatting import millify

# Legacy data.df_<name> -> how to obtain the same frame from datalayer.
FRAMES = {
    "df_viajeros": lambda: datalayer.travelers(),
    "df_viajeros_nacional": lambda: datalayer.travelers(TravelerKind.NATIONAL),
    "df_viajeros_internacional": lambda: datalayer.travelers(TravelerKind.INTERNATIONAL),
    "df_indicadores_turismo": lambda: datalayer.indicators_raw(),
}
FRAMES.update(
    {
        "df_" + name: (lambda name=name: datalayer.indicator(name))
        for name in datalayer.INDICATOR_NAMES
    }
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


def test_every_legacy_frame_is_covered():
    assert len(FRAMES) == 20


@pytest.mark.parametrize("name", sorted(FRAMES))
def test_dataframe_profile(name, snapshot_json):
    assert _profile(FRAMES[name]()) == snapshot_json


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
    assert millify(value) == expected


def test_create_options_dropdown():
    assert create_options_dropdown(2021) == {"label": "2021", "value": "2021"}


# Legacy card flag -> kind (note the inversion: 0 is international).
FLAG_KIND = {0: TravelerKind.INTERNATIONAL, 1: TravelerKind.NATIONAL, 2: None}


def _card_cases():
    # Same defaults the app offers: years/months in order of appearance in the data.
    df = datalayer.travelers()
    years = [int(y) for y in df["AÑO"].unique()[:2]]
    months = [m for m in df["MES"].unique() if m != "TOTAL"][:2]
    return [
        pytest.param(year, month, flag, id="%s-%s-flag%d" % (year, month, flag))
        for year in years
        for month in months
        for flag in (0, 1, 2)
    ]


def _call_card(fn, *args):
    try:
        return fn(*args)
    except Exception as exc:
        return {"error": type(exc).__name__, "message": str(exc)}


@pytest.mark.parametrize("year, month, flag", _card_cases())
def test_travel_card(year, month, flag, snapshot_json):
    assert _call_card(datalayer.travel_card, year, month, FLAG_KIND[flag]) == snapshot_json


@pytest.mark.parametrize("year, month, flag", _card_cases())
def test_pref_card(year, month, flag, snapshot_json):
    assert _call_card(datalayer.preference_card, year, month, FLAG_KIND[flag]) == snapshot_json
