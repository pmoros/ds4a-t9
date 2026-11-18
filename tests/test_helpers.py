"""The snapshot canonicaliser hides version noise, never real changes."""

import pandas as pd
import plotly.express as px

from helpers import dtype_kind, frame_hash, to_jsonable

FRAME = pd.DataFrame({"x": ["a", "b"], "y": [1, 2]})


def _fig(**kwargs):
    return to_jsonable(px.bar(FRAME, x="x", y="y", **kwargs))


def test_template_is_reduced_to_a_layout_digest():
    template = _fig()["layout"]["template"]
    assert isinstance(template, str) and template.startswith("sha256:")


def test_template_digest_ignores_per_trace_defaults_and_mapbox():
    base = {"layout": {"paper_bgcolor": "white"}, "data": {"bar": [1]}}
    noisy = {"layout": {"paper_bgcolor": "white", "mapbox": {"style": "x"}}, "data": {"bar": [2]}}
    assert to_jsonable({"template": base}) == to_jsonable({"template": noisy})


def test_template_digest_still_tells_themes_apart():
    assert (
        _fig(template="plotly")["layout"]["template"]
        != _fig(template="plotly_white")["layout"]["template"]
    )


def test_empty_fillpattern_is_dropped_but_a_real_one_is_kept():
    assert to_jsonable({"fillpattern": {"shape": ""}}) == {}
    assert to_jsonable({"fillpattern": {"shape": "/"}}) == {"fillpattern": {"shape": "/"}}


def test_value_changes_are_still_visible():
    assert _fig() != to_jsonable(px.bar(FRAME.assign(y=[1, 3]), x="x", y="y"))
    assert _fig() != _fig(labels={"y": "Total"})


def test_geojson_is_digested():
    assert to_jsonable({"geojson": {"a": 1}}) != to_jsonable({"geojson": {"a": 2}})


def test_text_columns_have_one_kind_whatever_the_storage():
    assert dtype_kind(FRAME["x"].dtype) == "text"
    assert dtype_kind(FRAME["x"].astype("string").dtype) == "text"
    assert dtype_kind(FRAME["y"].dtype) == "int64"


def test_frame_hash_ignores_text_storage_but_not_values():
    assert frame_hash(FRAME) == frame_hash(FRAME.astype({"x": "string"}))
    assert frame_hash(FRAME) != frame_hash(FRAME.assign(x=["a", "c"]))
    assert 0 <= int(frame_hash(FRAME)) < 2**64
