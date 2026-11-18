"""Page builders. Each page is a function, built on first call and cached.

Cached trees are shared between requests (and threads). That is safe because
nothing mutates a layout after it is built; Dash serialises it read-only.
"""

from dashboard.pages import about_us, home, indicators, travelers

PAGES = [
    home.home,
    travelers.who,
    travelers.preferences,
    indicators.accommodation,
    indicators.connectivity,
    indicators.economic,
    indicators.sightseeing,
    about_us.about_us,
]

_BUILDERS = [home._build, travelers._build, indicators._build, about_us._build]


def warm():
    """Build every page now, so missing or invalid data fails immediately."""
    for page in PAGES:
        page()


def clear_page_caches():
    for build in _BUILDERS:
        build.cache_clear()
