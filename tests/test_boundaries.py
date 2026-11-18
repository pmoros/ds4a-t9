"""AC5: callbacks and pages get data only through datalayer."""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
CALLERS = ["app.py"] + sorted(
    str(p.relative_to(REPO_ROOT)) for p in (REPO_ROOT / "dashboard").rglob("*.py")
)

FORBIDDEN = {
    "data frames from data.py": r"\bdata\.df_",
    "the old loader": r"\bwrangler\b",
    "traveler kind literals (use TravelerKind)": r"TURISTAS (NACIONALES|INTERNACIONALES)",
    "the copied national/international rule (use kind_from_clicks)": r"int\((inter)?national_bt\) > int",
    "source file paths": r"""["']data/|\.xlsx|\.csv|colombia\.geojson""",
}


@pytest.mark.parametrize("caller", CALLERS)
@pytest.mark.parametrize("what", sorted(FORBIDDEN))
def test_callers_do_not_reach_into_the_data(caller, what):
    source = (REPO_ROOT / caller).read_text(encoding="utf-8")
    hits = [
        "%s:%d: %s" % (caller, number, line.strip())
        for number, line in enumerate(source.splitlines(), 1)
        if re.search(FORBIDDEN[what], line)
    ]
    assert hits == [], "%s found:\n%s" % (what, "\n".join(hits))
