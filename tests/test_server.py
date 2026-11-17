"""AC3-AC5: production serving goes through gunicorn, configured by env."""

import os
import re
import runpy
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GUNICORN_CONF = REPO_ROOT / "gunicorn.conf.py"


def _conf(monkeypatch, **env):
    for name in ("PORT", "WEB_CONCURRENCY", "GUNICORN_THREADS"):
        monkeypatch.delenv(name, raising=False)
    for name, value in env.items():
        monkeypatch.setenv(name, value)
    return runpy.run_path(str(GUNICORN_CONF))


def test_gunicorn_defaults(monkeypatch):
    conf = _conf(monkeypatch)
    assert conf["bind"] == ["0.0.0.0:8050"]
    assert (conf["workers"], conf["threads"]) == (2, 4)
    assert conf["preload_app"] is True
    assert (conf["accesslog"], conf["errorlog"]) == ("-", "-")


def test_gunicorn_reads_environment(monkeypatch):
    conf = _conf(monkeypatch, PORT="9123", WEB_CONCURRENCY="3", GUNICORN_THREADS="8")
    assert conf["bind"] == ["0.0.0.0:9123"]
    assert (conf["workers"], conf["threads"]) == (3, 8)


def test_gunicorn_rejects_bad_port(monkeypatch):
    with pytest.raises(ValueError, match="PORT"):
        _conf(monkeypatch, PORT="http")


# --------------------------------------------------------------------------
# AC5: no debug server on production paths
# --------------------------------------------------------------------------

PRODUCTION_ENTRYPOINTS = ["Dockerfile", "Procfile", "deploy_app.sh"]


@pytest.mark.parametrize("entrypoint", PRODUCTION_ENTRYPOINTS)
def test_entrypoints_use_gunicorn_with_its_config(entrypoint):
    text = (REPO_ROOT / entrypoint).read_text(encoding="utf-8")
    assert not re.search(r"python3?\s+app\.py|\"python\",\s*\"app\.py\"", text)
    assert "gunicorn" in text and "gunicorn.conf.py" in text


def test_debug_is_never_hardcoded():
    assert "debug=True" not in (REPO_ROOT / "app.py").read_text(encoding="utf-8")


# --------------------------------------------------------------------------
# AC4: a real gunicorn process serves the app on $PORT
# --------------------------------------------------------------------------


def _free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _get(url):
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.status


def test_gunicorn_serves_the_app(tmp_path):
    port = _free_port()
    env = dict(os.environ, PORT=str(port), WEB_CONCURRENCY="1", GUNICORN_THREADS="2")
    log = (tmp_path / "gunicorn.log").open("w+")
    gunicorn = Path(sys.executable).with_name("gunicorn")
    process = subprocess.Popen(
        [str(gunicorn), "-c", "gunicorn.conf.py", "app:server"],
        cwd=str(REPO_ROOT),
        env=env,
        stdout=log,
        stderr=subprocess.STDOUT,
    )
    try:
        base = "http://127.0.0.1:%d" % port
        deadline = time.monotonic() + 90
        while True:
            try:
                assert _get(base + "/") == 200
                break
            except OSError:
                if process.poll() is not None or time.monotonic() > deadline:
                    log.seek(0)
                    pytest.fail("gunicorn did not serve on %s:\n%s" % (base, log.read()))
                time.sleep(0.5)
        assert _get(base + "/_dash-layout") == 200
    finally:
        process.send_signal(signal.SIGTERM)
        try:
            process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
        log.close()
    assert process.returncode == 0, "gunicorn did not shut down cleanly"
