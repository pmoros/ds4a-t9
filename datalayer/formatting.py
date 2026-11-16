"""Number formatting shared by the summary cards."""

import numpy as np

MILLNAMES = ["", " K", " M", " B", " T"]


def millify(n):
    """Compact form of a number: 1_234_567 -> "1 M" (rounds half to even)."""
    n = float(n)
    millidx = max(
        0,
        min(len(MILLNAMES) - 1, int(np.floor(0 if n == 0 else np.log10(abs(n)) / 3))),
    )
    return "{:.0f}{}".format(n / 10 ** (3 * millidx), MILLNAMES[millidx])
