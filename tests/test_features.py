# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Tests for dashboard route."""

from __future__ import annotations

from fastapi.testclient import TestClient

from lct_web.main import app

CLUB_TYPES = ["Lunar", "LunarII"]


client = TestClient(app)


def test_features_lunar() -> None:
    response = client.get("/features/Lunar")

    assert response.status_code == 200
    features = response.json()
    assert len(features["features"]) == 13
    assert len(features["features"]["Crater"]) == 55


def test_features_lunarII() -> None:
    response = client.get("/features/LunarII")

    assert response.status_code == 200
    features = response.json()
    assert len(features["features"]) == 13
    assert len(features["features"]["Mons"]) == 10


def test_features_bad_path() -> None:
    response = client.get("/features/Hello")

    assert response.status_code == 422
