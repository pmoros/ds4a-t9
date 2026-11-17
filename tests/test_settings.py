"""AC1/AC2: server settings come from the environment, with safe defaults."""

import pytest

import settings


def test_defaults_are_safe():
    s = settings.load({})
    assert (s.host, s.port, s.debug) == ("127.0.0.1", 8050, False)


def test_values_from_environment():
    s = settings.load({"PORT": "9000", "HOST": "0.0.0.0", "DASH_DEBUG": "TRUE"})
    assert (s.host, s.port, s.debug) == ("0.0.0.0", 9000, True)


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("1", True),
        ("yes", True),
        ("On", True),
        ("true", True),
        ("0", False),
        ("no", False),
        ("OFF", False),
        ("false", False),
        ("", False),
    ],
)
def test_debug_flag_spellings(raw, expected):
    assert settings.load({"DASH_DEBUG": raw}).debug is expected


@pytest.mark.parametrize(
    "env, variable",
    [
        ({"PORT": "abc"}, "PORT"),
        ({"PORT": "0"}, "PORT"),
        ({"PORT": "65536"}, "PORT"),
        ({"DASH_DEBUG": "maybe"}, "DASH_DEBUG"),
    ],
)
def test_invalid_values_name_the_variable(env, variable):
    with pytest.raises(ValueError, match=variable):
        settings.load(env)


def test_reads_os_environ_by_default(monkeypatch):
    monkeypatch.setenv("PORT", "8123")
    assert settings.load().port == 8123
