"""Characterization snapshots for all Dash callbacks.

Each callback is run with the values the browser would send on first load,
for both traveler types. Results (figures, card texts, dropdown options, and
also exceptions) are snapshotted, so any behaviour change shows up as a diff.
Update intentionally with ``pytest --snapshot-update``.
"""

import pytest

import app as legacy
from helpers import SCENARIOS, callback_id, run_callbacks

CALLBACK_KEYS = sorted(legacy.app.callback_map)

_cache = {}


def _results(scenario):
    if scenario not in _cache:
        _cache[scenario] = run_callbacks(legacy, SCENARIOS[scenario])
    return _cache[scenario]


def test_callback_count():
    assert len(CALLBACK_KEYS) == 54


@pytest.mark.parametrize("scenario", sorted(SCENARIOS))
def test_callback_chain_converges(scenario):
    _, passes = _results(scenario)
    assert passes <= 3


@pytest.mark.parametrize("scenario", sorted(SCENARIOS))
@pytest.mark.parametrize("output_key", CALLBACK_KEYS, ids=[callback_id(k) for k in CALLBACK_KEYS])
def test_callback_output(scenario, output_key, snapshot_json):
    results, _ = _results(scenario)
    assert results[output_key] == snapshot_json
