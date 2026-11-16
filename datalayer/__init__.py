"""Data access for the IDT dashboard.

The only code that knows where the source files are, what their columns are
called and how they are cleaned. Nothing is read at import time; sources are
loaded on first use and cached.

Returned frames are shared, cached objects: filter or copy them, never modify
them in place (that would change what every later request sees).
"""

from .indicators import NAMES as INDICATOR_NAMES
from .indicators import indicator
from . import indicators as _indicators
from . import sources as _sources
from .schema import TravelerKind
from .sources import DataSchemaError, load_geojson, load_indicators
from .travelers import (
    kind_from_clicks,
    options,
    preference_card,
    strip_prefix,
    travel_card,
    travelers,
)

indicators_raw = load_indicators


def clear_caches():
    """Forget every loaded source and derived frame (tests, data reloads)."""
    for cached in _sources.CACHED_READERS + (_indicators._build,):
        cached.cache_clear()


__all__ = [
    "INDICATOR_NAMES",
    "DataSchemaError",
    "TravelerKind",
    "clear_caches",
    "indicator",
    "indicators_raw",
    "kind_from_clicks",
    "load_geojson",
    "options",
    "preference_card",
    "strip_prefix",
    "travel_card",
    "travelers",
]
