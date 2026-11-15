"""Shared fixtures for the characterization test-suite.

The legacy modules read data through paths relative to the repository root
and load everything at import time, so we pin the working directory and the
import path here, before any test module imports ``app``.
"""

import os
import sys
from pathlib import Path

import pytest
from syrupy.extensions.json import JSONSnapshotExtension

REPO_ROOT = Path(__file__).resolve().parent.parent

os.chdir(REPO_ROOT)
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@pytest.fixture
def snapshot_json(snapshot):
    """One readable JSON snapshot file per test, so diffs stay reviewable."""
    return snapshot.use_extension(JSONSnapshotExtension)


@pytest.fixture(scope="session")
def legacy_app():
    import app

    return app


@pytest.fixture(scope="session")
def client(legacy_app):
    return legacy_app.server.test_client()
