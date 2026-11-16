"""Tourism indicators: one declarative spec per frame the dashboard uses.

Replaces the copy-pasted blocks that used to live in data.py. Each simple spec
runs the same pipeline, in this order:

    theme filter -> VARIABLE filter -> drop columns -> parse VALOR
    -> frame-wide replaces (in order) -> row filter

The two occupancy-rate series need a different step order and are written as
builder functions instead.
"""

from dataclasses import dataclass, replace
from functools import lru_cache
from typing import Callable, Optional, Tuple

import pandas as pd

from . import config, sources
from .schema import CLASS, MONTH, SOURCE, SUBTHEME, THEME, VALUE, VARIABLE, YEAR, YEAR_MONTH

FLOAT = "float"
PERCENT = "percent"  # strings like "61.1%"


@dataclass(frozen=True)
class IndicatorSpec:
    theme: str
    drop: Tuple[str, ...]
    value: Optional[str] = FLOAT  # FLOAT, PERCENT, or None to leave VALOR as is
    variables: Optional[Tuple[str, ...]] = None  # keep only these VARIABLE values
    renames: Tuple[Tuple[str, str], ...] = ()  # (old, new), replaced frame-wide
    rows: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = None

    def build(self, raw):
        df = raw.copy()
        df = df[df[THEME] == self.theme]
        if self.variables is not None:
            df = df[df[VARIABLE].isin(list(self.variables))]
        df = df.drop(list(self.drop), axis=1)
        if self.value is not None:
            df[VALUE] = _parse_value(df[VALUE], self.value)
        for old, new in self.renames:
            df = df.replace({old: new})
        if self.rows is not None:
            df = self.rows(df)
        return df


def _parse_value(values, kind):
    if kind == PERCENT:
        return values.str.rstrip("%").astype(float)
    return values.astype(float)


# -- simple specs -----------------------------------------------------------

_GENERACION_EMPLEO = IndicatorSpec(
    theme="Generación de empleo turismo",
    drop=(THEME, CLASS, SOURCE),
    value=PERCENT,
)

_PRESTADORES = IndicatorSpec(
    theme="Prestadores de Servicios Turísticos - PST",
    variables=("Total",),
    drop=(THEME, CLASS, SOURCE, MONTH, VARIABLE),
    renames=(
        ("Establecimiento de gastronomia y similares", "Establecimiento gastronomico"),
        ("Establecimiento de alojamiento y hospedaje", "Alojamiento"),
        (
            "Arrendadores de vehiculos para turismo nacional e internacional",
            "Arrendadores de vehiculos",
        ),
        (
            "Empresas captadoras de ahorro para viajes y de servicios turisticos",
            "Empresas captadoras de ahorro para servicios turisticos",
        ),
        (
            "Usuarios operadores, desarrolladores e industriales en zonas francas turísticas",
            "Usuarios operadores en zonas francas turísticas",
        ),
    ),
)

_TURISMO_INTERNACIONAL = "Informacion Destacada del turismo internacional"

SPECS = {
    "airbnb_homeway": IndicatorSpec(
        theme="Airbnb & Homeaway",
        drop=(THEME, VARIABLE, CLASS, SOURCE, MONTH),
    ),
    "bigdata": IndicatorSpec(theme="Big Data", drop=(THEME, SOURCE, MONTH)),
    "cert_turismo_sostenible": IndicatorSpec(
        theme="Certificación de Turismo Sostenible",
        drop=(THEME, SOURCE, MONTH),
        renames=(
            ("Sedes para eventos, congresos, ferias y convenciones", "Sedes para eventos"),
            ("Establecimientos gastronómicos y bares", "Establecimientos gastronómicos"),
        ),
    ),
    "conect_internacional": IndicatorSpec(
        theme="Conectividad directa internacional",
        drop=(THEME, CLASS, SOURCE, MONTH),
    ),
    # Yearly rows only; the monthly rows are gen_empleo_turismo2.
    "gen_empleo_turismo": replace(_GENERACION_EMPLEO, rows=lambda df: df[df[MONTH].isnull()]),
    "gen_empleo_turismo2": replace(_GENERACION_EMPLEO, rows=lambda df: df[df[MONTH].notnull()]),
    "indice_competitividad_turistica": IndicatorSpec(
        theme="Índice de Competitividad Turística Regional de Colombia-ICTRC",
        drop=(THEME, CLASS, SOURCE, MONTH),
    ),
    "indice_presion_turistica": IndicatorSpec(
        theme="Índice de Presión Turística",
        drop=(THEME, SUBTHEME, VARIABLE, CLASS, SOURCE, MONTH),
    ),
    "turismo_internacional": IndicatorSpec(
        theme=_TURISMO_INTERNACIONAL,
        variables=(
            "Exportaciones Totales de Turismo Internacional",
            "Ingresos por turismo internacional",
            "Llegadas de Turistas Internacionales",
            "Transporte Internacional de Pasajeros",
        ),
        drop=(THEME, SOURCE, MONTH),
    ),
    "turismo_internacional2": IndicatorSpec(
        theme=_TURISMO_INTERNACIONAL,
        variables=("Proposito del Viaje", "Medio de Transporte"),
        drop=(THEME, SOURCE, MONTH),
        value=PERCENT,
    ),
    "pib": IndicatorSpec(
        theme="PIB",
        drop=(THEME, SUBTHEME, VARIABLE, SOURCE, MONTH),
        value=None,
        renames=(
            (
                "Sector: Comercio al por mayor y al por menor; reparación de vehículos "
                "automotores y motocicletas; Transporte y almacenamiento; Alojamiento y "
                "servicios de comida/ PIB Bogotá",
                "Sector: Alojamiento y comida",
            ),
            (
                "Subsector: Alojamiento y servicio de comida/ PIB Bogotá",
                "Subsector: Alojamiento y comida",
            ),
        ),
    ),
    "prest_servicios_turisticos": _PRESTADORES,
    # Split by size so each chart has a readable scale (rows == 400 are in neither).
    "prest_servicios_turisticos1": replace(_PRESTADORES, rows=lambda df: df.query("VALOR>400")),
    "prest_servicios_turisticos2": replace(_PRESTADORES, rows=lambda df: df.query("VALOR<400")),
}


# -- builders with their own step order -------------------------------------


def _tasa_ocupacion_airbnb(raw):
    df = raw.copy()
    df = df[df[THEME] == "Tasa de ocupación Airbnb"]
    df = df.drop([THEME, VARIABLE, CLASS, SOURCE], axis=1)
    df[YEAR_MONTH] = df[YEAR].map(str) + "-" + df[MONTH]
    df[MONTH] = pd.to_numeric(df[MONTH])
    df = df.query("MES>0").copy()
    df[VALUE] = _parse_value(df[VALUE], PERCENT)
    return df


def _tasa_ocupacion_hotelera(raw):
    df = raw.copy()
    df = df[df[THEME] == "Tasa de ocupación Hotelera"]
    df = df.drop([THEME, VARIABLE, CLASS, SOURCE], axis=1)
    df[MONTH] = df[MONTH].map(str)
    df = df.query("MES!='nan'").copy()
    df[YEAR_MONTH] = df[YEAR].map(str) + "-" + df[MONTH]
    df[VALUE] = _parse_value(df[VALUE], PERCENT)
    return df


BUILDERS = {name: spec.build for name, spec in SPECS.items()}
BUILDERS["tasa_ocupacion_airbnb"] = _tasa_ocupacion_airbnb
BUILDERS["tasa_ocupacion_hotelera"] = _tasa_ocupacion_hotelera

NAMES = tuple(sorted(BUILDERS))


def indicator(name):
    """The cleaned frame for one indicator (see NAMES)."""
    if name not in BUILDERS:
        raise KeyError("unknown indicator %r; known: %s" % (name, ", ".join(NAMES)))
    return _build(name, str(config.indicators_path()))


@lru_cache(maxsize=None)
def _build(name, path):  # path is part of the cache key only
    return BUILDERS[name](sources.load_indicators())
