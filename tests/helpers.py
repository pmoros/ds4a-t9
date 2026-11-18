"""Helpers to drive the legacy Dash app without a browser.

* ``to_jsonable`` turns figures / Dash components into plain, stable JSON.
* ``initial_props`` collects every component prop declared in the layouts.
* ``run_callbacks`` emulates Dash's initial callback chain: it feeds each
  callback the current prop values, writes its outputs back, and repeats until
  nothing changes (dropdown options/values set by "menu" callbacks feed the
  graph callbacks, as they do in the browser).
"""

import base64
import hashlib
import json
import re

import numpy as np
import pandas as pd
import plotly.utils
from dash.development.base_component import Component

# Every route handled by app.display_page.
PAGE_PATHS = [
    "/",
    "/travelers/who",
    "/travelers/preferences",
    "/indicators/accomodation",
    "/indicators/connectivity",
    "/indicators/economic",
    "/indicators/sightseeing",
    "/about-us",
]

NATIONAL_BUTTON = "viajeros-selector-national"
INTERNATIONAL_BUTTON = "viajeros-selector-international"

# The traveler-type toggle compares the buttons' n_clicks_timestamp values.
SCENARIOS = {
    "national": {},  # layout default: both timestamps '0' -> national
    "international": {
        (NATIONAL_BUTTON, "n_clicks_timestamp"): "1",
        (INTERNATIONAL_BUTTON, "n_clicks_timestamp"): "2",
    },
}

MAX_PASSES = 6

# Snapshots must not depend on the library versions that produced them, so
# representation that changes between releases is canonicalised here. Each rule
# is covered by tests/test_helpers.py, including cases that must still differ.
#
# * geojson: a large blob, stored as a digest.
# * template: plotly's theme. Its ``data`` part holds per-trace defaults that
#   change every release; ``layout`` is what makes a theme look the way it does
#   (backgrounds, grids, colorway, fonts), so only that is digested. ``mapbox``
#   is left out because plotly renamed the map style defaults.
# * fillpattern {"shape": ""} on traces: an empty default newer plotly emits.
# * {"bdata", "dtype"[, "shape"]}: plotly >= 6 sends numpy arrays base64-encoded;
#   decoded back to plain lists (lossless).


def _digest(value):
    raw = json.dumps(value, sort_keys=True).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _template_digest(template):
    layout = {k: v for k, v in template.get("layout", {}).items() if k != "mapbox"}
    return _digest(layout)


_NUMPY_DTYPES = {"f8": "<f8", "f4": "<f4", "i1": "i1", "u1": "u1", "i2": "<i2"}
_NUMPY_DTYPES.update({"u2": "<u2", "i4": "<i4", "u4": "<u4", "i8": "<i8", "u8": "<u8"})


def _decode_typed_array(value):
    array = np.frombuffer(base64.b64decode(value["bdata"]), dtype=_NUMPY_DTYPES[value["dtype"]])
    if "shape" in value:
        shape = [int(n) for n in str(value["shape"]).split(",")]
        array = array.reshape(shape)
    return array.tolist()


def _is_typed_array(value):
    return isinstance(value, dict) and set(value) - {"shape"} == {"bdata", "dtype"}


def _scrub(value):
    if _is_typed_array(value):
        return _decode_typed_array(value)
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key == "geojson":
                out[key] = _digest(item)
            elif key == "template" and isinstance(item, dict):
                out[key] = _template_digest(item)
            elif key == "fillpattern" and item == {"shape": ""}:
                continue
            else:
                out[key] = _scrub(item)
        return out
    if isinstance(value, list):
        return [_scrub(v) for v in value]
    return value


def to_jsonable(obj):
    raw = json.dumps(obj, cls=plotly.utils.PlotlyJSONEncoder, sort_keys=True)
    return _scrub(json.loads(raw))


def slug(text):
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_")


def iter_components(root):
    if not isinstance(root, Component):
        return
    yield root
    for child in root._traverse():
        if isinstance(child, Component):
            yield child


def display_page(app_module, pathname):
    """Call the router directly (``app.display_page`` is the plain function)."""
    return app_module.display_page(pathname)


def page_layouts(app_module):
    return {path: display_page(app_module, path) for path in PAGE_PATHS}


def initial_props(app_module):
    roots = [app_module.app.layout, *page_layouts(app_module).values()]
    props = {}
    for root in roots:
        for comp in iter_components(root):
            comp_id = getattr(comp, "id", None)
            if comp_id is None:
                continue
            for prop, value in comp.to_plotly_json()["props"].items():
                props.setdefault((comp_id, prop), value)
    return props


def parse_outputs(output_key):
    """'a.figure' -> [('a', 'figure')]; '..a.x...b.y..' -> [('a','x'), ('b','y')]."""
    parts = output_key[2:-2].split("...") if output_key.startswith("..") else [output_key]
    return [tuple(part.rsplit(".", 1)) for part in parts]


def callback_id(output_key):
    """Short, filesystem-safe test id: first output plus the count of the rest."""
    outputs = parse_outputs(output_key)
    first = slug("-".join(outputs[0]))
    return first if len(outputs) == 1 else "%s__plus%d" % (first, len(outputs) - 1)


def _call(spec, state):
    deps = spec["inputs"] + spec["state"]
    args = [state.get((d["id"], d["property"])) for d in deps]
    try:
        return True, spec["callback"].__wrapped__(*args)
    except Exception as exc:  # characterize failures too
        return False, {"error": type(exc).__name__, "message": str(exc)}


def run_callbacks(app_module, overrides):
    """Return ({output_key: jsonable result}, passes_needed)."""
    results, passes, _ = settle_callbacks(app_module, overrides)
    return results, passes


def call_callback(spec, state):
    """Run one callback_map entry against ``state``: (ok, value or error dict)."""
    return _call(spec, state)


def settle_callbacks(app_module, overrides):
    """Like run_callbacks, but also return the settled {(id, prop): value} state."""
    state = initial_props(app_module)
    # dcc.Location only gets its pathname from the browser; emulate landing on "/".
    state[("url", "pathname")] = "/"
    state.update(overrides)
    callback_map = app_module.app.callback_map

    previous = None
    for passes in range(1, MAX_PASSES + 1):
        results = {}
        for key, spec in callback_map.items():
            ok, value = _call(spec, state)
            results[key] = to_jsonable(value)
            if not ok:
                continue
            outputs = parse_outputs(key)
            values = [value] if len(outputs) == 1 else list(value)
            for target, out_value in zip(outputs, values, strict=False):
                state[target] = out_value
        if results == previous:
            return results, passes, state
        previous = results
    raise AssertionError("callback chain did not converge in %d passes" % MAX_PASSES)


# --------------------------------------------------------------------------
# DataFrame profiles (independent of the pandas version)
# --------------------------------------------------------------------------


def _is_text(dtype):
    # pandas 1 stores strings as object; pandas 3 has a dedicated str dtype.
    return pd.api.types.is_object_dtype(dtype) or pd.api.types.is_string_dtype(dtype)


def dtype_kind(dtype):
    return "text" if _is_text(dtype) else str(dtype)


def frame_hash(df):
    """Content hash that only depends on the values, not on how text is stored."""
    text = [col for col, dtype in df.dtypes.items() if _is_text(dtype)]
    canonical = df.astype({col: object for col in text})
    return str(int(pd.util.hash_pandas_object(canonical, index=True).sum()) % 2**64)
