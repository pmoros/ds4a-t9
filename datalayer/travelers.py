"""Travelers survey data: filtering by kind, menu options and summary cards."""

from . import sources
from .formatting import millify
from .schema import (
    ITEM,
    MONTH,
    ORIGIN,
    SUBTHEME,
    THEME,
    TRAVELERS,
    YEAR,
    TravelerKind,
)


def travelers(kind=None):
    """All travelers, or only one TravelerKind. Rows keep their original index."""
    df = sources.load_travelers()
    if kind is None:
        return df
    return df[df[THEME] == TravelerKind(kind).value]


def options(column, kind=None):
    """Distinct values of ``column`` in source order (for dropdown menus)."""
    return travelers(kind)[column].unique()


def kind_from_clicks(national_ts, international_ts):
    """Which kind the national/international buttons select.

    Dash passes each button's last-click timestamp (0 if never clicked); the
    most recent click wins and a tie means national.
    """
    if int(international_ts) > int(national_ts):
        return TravelerKind.INTERNATIONAL
    return TravelerKind.NATIONAL


def strip_prefix(label):
    """Drop the source's ordering prefix: "A. HOMBRE" -> "HOMBRE"."""
    return label[3:]


def _for_period(year, month, kind):
    df = travelers()
    df = df.loc[df[YEAR] == year].loc[df[MONTH] == month]
    if kind is not None:
        df = df.loc[df[THEME] == TravelerKind(kind).value]
    return df


def _ranked(df, subtheme, exclude=None):
    rows = df.loc[df[SUBTHEME] == subtheme]
    if exclude is not None:
        rows = rows.drop(index=rows.loc[rows[ITEM] == exclude].index)
    return rows.groupby(ITEM).sum().sort_values(by=TRAVELERS, ascending=False).reset_index()


def _top_share(ranked):
    """(share of the top item as "NN%", top item label without prefix)."""
    share = int(ranked.iloc[0][TRAVELERS] / ranked[TRAVELERS].sum() * 100)
    return str(int(share)) + "%", strip_prefix(ranked[[ITEM, TRAVELERS]].iloc[0][ITEM])


def _top_label(ranked):
    return strip_prefix(ranked[[ITEM, TRAVELERS]].iloc[0][ITEM])


def travel_card(year, month, kind=None):
    """Who travels: totals, gender split, top origin, education and age.

    ``kind=None`` combines national and international travelers.
    """
    df = _for_period(year, month, kind)

    total = df.groupby([YEAR, MONTH]).sum()
    total = millify(total.reset_index(drop=True)[TRAVELERS][0])

    gender = df.loc[df[SUBTHEME] == "GENERO"]
    male = gender.loc[df[ITEM] == "A. HOMBRE"]
    gender = gender.drop(index=gender.loc[gender[ITEM] == "C. NS/NR"].index)
    gender_total = gender.groupby([YEAR, MONTH]).sum().reset_index(drop=True)[TRAVELERS][0]
    male = male.groupby([YEAR, MONTH]).sum()
    male = int((male.reset_index(drop=True)[TRAVELERS][0] / gender_total) * 100)
    female = 100 - male

    origin = df.groupby(ORIGIN).sum().sort_values(by=TRAVELERS, ascending=False).reset_index()
    origin = origin[[ORIGIN, TRAVELERS]].iloc[0][ORIGIN]

    return {
        "Total travelers": total,
        "Travelers gender": [str(int(male)) + "%", "Men", str(int(female)) + "%", "Women"],
        "Origin": origin,
        "Education level": _top_label(_ranked(df, "EDUCACION", exclude="G. NS/NR")),
        "Age": _top_label(_ranked(df, "EDAD", exclude="A. NS/NR")),
    }


def preference_card(year, month, kind=None):
    """What travelers prefer: purpose, attraction, group, accommodation, expense.

    ``kind=None`` combines national and international travelers.
    """
    df = _for_period(year, month, kind)
    return {
        "Trip purpose": list(_top_share(_ranked(df, "MOTIVO"))),
        "Most visited tourist attraction": list(_top_share(_ranked(df, "ATRACTIVOS"))),
        "Travel group": _top_label(_ranked(df, "GRUPO")),
        "accommodation": _top_label(_ranked(df, "ALOJAMIENTO")),
        "Higher expense": _top_label(_ranked(df, "GASTO DISTRI")),
    }
