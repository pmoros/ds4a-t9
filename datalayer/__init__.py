"""Data access for the IDT dashboard.

The only code that knows where the source files are, what their columns are
called and how they are cleaned. Nothing is read at import time; sources are
loaded on first use and cached.
"""

from .indicators import NAMES as INDICATOR_NAMES
from .indicators import indicator
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

__all__ = [
    "INDICATOR_NAMES",
    "DataSchemaError",
    "TravelerKind",
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
