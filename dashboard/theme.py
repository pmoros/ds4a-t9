"""Colours, palettes and month ordering shared by pages and callbacks."""

MAIN_COLOR_CONTRAST = "#20284D"

# The stray space in " #BADA55" is legacy and appears in the snapshots; it is
# fixed in the hygiene phase as a visible change.
COLOR_PALETTE_DISCRETE = ["#20284D", "#4A589B", "#D4D4E9", "#BADA55", "#FFE787", "#B8B97E", "#D36135", "#F49D6E", "#4C8577"]  # fmt: skip
COLOR_PALETTE_DISCRETE_2 = ["#20284D", " #BADA55", "#4A589B", "#BADA55", "#FFE787", "#B8B97E", "#D36135", "#F49D6E", "#4C8577"]  # fmt: skip
COLOR_PALETTE_CONTINUOUS = ["#20284D", "#4A589B", "#D4D4E9", "#BADA55"]

MESES_ORDEN = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12,
}
