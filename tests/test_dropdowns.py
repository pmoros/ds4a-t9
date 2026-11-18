"""Clearing a dropdown must never crash a callback (it used to answer HTTP 500).

* A single-select dropdown drives a callback that needs exactly one value, so
  it is not clearable: the browser can never send ``None`` for it.
* A cleared multi-select sends ``[]``; every callback it feeds must cope.
"""

import pytest
from dash import dcc
from helpers import SCENARIOS, call_callback, iter_components, page_layouts, settle_callbacks

import app as legacy


def _dropdowns():
    found = {}
    for root in page_layouts(legacy).values():
        for comp in iter_components(root):
            if isinstance(comp, dcc.Dropdown):
                found.setdefault(comp.id, []).append(comp)
    return found


DROPDOWNS = _dropdowns()
SINGLE = sorted(i for i, comps in DROPDOWNS.items() if not getattr(comps[0], "multi", False))
MULTI = sorted(i for i, comps in DROPDOWNS.items() if getattr(comps[0], "multi", False))


def test_both_kinds_exist():
    assert len(SINGLE) == 6
    assert len(MULTI) == 45


@pytest.mark.parametrize("component_id", SINGLE)
def test_single_select_cannot_be_cleared(component_id):
    assert all(comp.clearable is False for comp in DROPDOWNS[component_id])


_settled = {}


def _state(scenario):
    if scenario not in _settled:
        _settled[scenario] = settle_callbacks(legacy, SCENARIOS[scenario])[2]
    return _settled[scenario]


def _consumers(component_id):
    return {
        key: spec
        for key, spec in legacy.app.callback_map.items()
        if any(d["id"] == component_id and d["property"] == "value" for d in spec["inputs"])
    }


@pytest.mark.parametrize("scenario", sorted(SCENARIOS))
@pytest.mark.parametrize("component_id", MULTI)
def test_clearing_a_multi_select_never_raises(scenario, component_id):
    state = dict(_state(scenario))
    state[(component_id, "value")] = []
    failures = {}
    for key, spec in _consumers(component_id).items():
        ok, value = call_callback(spec, state)
        if not ok:
            failures[key] = value
    assert failures == {}
