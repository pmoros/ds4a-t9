"""Names that come from the source files: columns and category values."""

from enum import Enum

# Columns (travelers and indicators share some of them).
YEAR = "AÑO"
MONTH = "MES"
THEME = "TEMA"
SUBTHEME = "SUBTEMA"
ITEM = "ITEM"
TRAVELERS = "VIAJEROS"
ORIGIN = "ORIGEN"
VARIABLE = "VARIABLE"
CLASS = "CLASE"
SOURCE = "FUENTE"
VALUE = "VALOR"
YEAR_MONTH = "AÑO-MES"  # derived for the occupancy-rate series

TRAVELERS_COLUMNS = (YEAR, MONTH, THEME, SUBTHEME, ITEM, TRAVELERS, ORIGIN)
INDICATORS_COLUMNS = (THEME, SUBTHEME, VARIABLE, CLASS, SOURCE, YEAR, MONTH, VALUE)


class TravelerKind(str, Enum):
    """Values of the travelers' TEMA column. Compare with ``.value``."""

    NATIONAL = "TURISTAS NACIONALES"
    INTERNATIONAL = "TURISTAS INTERNACIONALES"
