"""Raw readers for the source files: cached per path and validated.

Nothing is read at import time. Each loader resolves its path from the
environment on every call and reads through a cache keyed on that path, so
changing IDT_DATA_DIR takes effect without stale results.
"""

import json
from functools import lru_cache
from pathlib import Path

import pandas as pd

from . import config
from .schema import INDICATORS_COLUMNS, TRAVELERS_COLUMNS


class DataSchemaError(ValueError):
    """A source file is missing columns the dashboard needs."""


def _check_exists(path):
    if not path.is_file():
        raise FileNotFoundError(
            "data file not found: %s (set IDT_DATA_DIR / IDT_GEOJSON_PATH)" % path
        )


def _require_columns(df, required, path):
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise DataSchemaError("%s is missing columns: %s" % (Path(path).name, ", ".join(missing)))


@lru_cache(maxsize=None)
def _read_travelers(path):
    df = pd.read_excel(path)
    _require_columns(df, TRAVELERS_COLUMNS, path)
    return df


@lru_cache(maxsize=None)
def _read_indicators(path):
    df = pd.read_csv(path)
    df.columns = [column.upper() for column in df.columns]
    _require_columns(df, INDICATORS_COLUMNS, path)
    return df


@lru_cache(maxsize=None)
def _read_geojson(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


CACHED_READERS = (_read_travelers, _read_indicators, _read_geojson)


def clear_caches():
    for reader in CACHED_READERS:
        reader.cache_clear()


def load_travelers():
    path = config.travelers_path()
    _check_exists(path)
    return _read_travelers(str(path))


def load_indicators():
    path = config.indicators_path()
    _check_exists(path)
    return _read_indicators(str(path))


def load_geojson():
    path = config.geojson_path()
    _check_exists(path)
    return _read_geojson(str(path))
