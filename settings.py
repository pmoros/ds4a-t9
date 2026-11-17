"""Server settings, read from the environment (12-factor).

    PORT        port to listen on (default 8050)
    HOST        interface for the development server (default 127.0.0.1)
    DASH_DEBUG  enable Dash's debug mode and reloader (default false);
                never enable it on a reachable host: the debugger runs code

Production runs through gunicorn (see gunicorn.conf.py), which reads PORT too.
"""

import os
from dataclasses import dataclass

TRUE = {"1", "true", "yes", "on"}
FALSE = {"0", "false", "no", "off", ""}


@dataclass(frozen=True)
class Settings:
    host: str
    port: int
    debug: bool


def port_from(env, default=8050):
    raw = env.get("PORT", str(default))
    try:
        port = int(raw)
    except ValueError:
        raise ValueError("PORT must be an integer, got %r" % raw) from None
    if not 1 <= port <= 65535:
        raise ValueError("PORT must be between 1 and 65535, got %d" % port)
    return port


def _flag(env, name, default=False):
    raw = env.get(name)
    if raw is None:
        return default
    value = raw.strip().lower()
    if value in TRUE:
        return True
    if value in FALSE:
        return False
    raise ValueError(
        "%s must be one of %s, got %r" % (name, "/".join(sorted(TRUE | FALSE - {""})), raw)
    )


def load(env=None):
    env = os.environ if env is None else env
    return Settings(
        host=env.get("HOST", "127.0.0.1"),
        port=port_from(env),
        debug=_flag(env, "DASH_DEBUG"),
    )
