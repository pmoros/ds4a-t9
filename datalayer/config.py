"""Where the data lives.

Paths come from the environment (12-factor), with defaults resolved from this
package's location, never from the current working directory.

    IDT_DATA_DIR      directory holding the travelers and indicators files
    IDT_GEOJSON_PATH  geojson with Colombia's departments (national map)
"""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

TRAVELERS_FILE = "base_viajeros.xlsx"
INDICATORS_FILE = "2. Base de Indicadores de Turismo 2.csv"


def data_dir():
    return Path(os.environ.get("IDT_DATA_DIR") or REPO_ROOT / "data")


def travelers_path():
    return data_dir() / TRAVELERS_FILE


def indicators_path():
    return data_dir() / INDICATORS_FILE


def geojson_path():
    return Path(os.environ.get("IDT_GEOJSON_PATH") or REPO_ROOT / "assets" / "colombia.geojson")
