# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Tests for lunar_two routes."""

from __future__ import annotations

from fastapi.testclient import TestClient
from lct_web.main import app

client = TestClient(app)

def test_lunar_two() -> None:
    response = client.get("/lunar_two",
                          params = {
                            "date": 1382133600.0,
                            "lat": 35.9694444444444,
                            "lon": -84.316666666666
                          })
    assert response.status_code == 200
    lunar_two_info = response.json()
    assert len(lunar_two_info["features"]) == 11
    assert len(lunar_two_info["landing_sites"]) == 16
