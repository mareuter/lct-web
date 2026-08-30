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

from . import constants

client = TestClient(app)


def test_dashboard() -> None:
    response = client.get(
        "/dashboard",
        params=constants.DATE_LOC_TZ_PARAMS,
    )
    assert response.status_code == 200
    dashboard_info = response.json()
    assert dashboard_info["age"] == 13.892695999260468
    assert dashboard_info["colong"] == 83.97189956624061
    assert dashboard_info["fractional_phase"] == 0.9998519924481626
    assert dashboard_info["azimuth"] == 69.75156520051686
    assert dashboard_info["phase"] == "Full Moon"
    next_phase = dashboard_info["next_phase"]
    assert len(next_phase) == 1
    assert next_phase[0]["id"] == 0
    assert next_phase[0]["phase"] == "full_moon"
    assert next_phase[0]["datetime"] == [2013, 10, 18, 23, 37, 39.633078]
    assert dashboard_info["lunar_club"]["naked_eye"] == 10
    assert dashboard_info["lunar_club"]["binocular"] == 2
    assert dashboard_info["lunar_club"]["telescope"] == 0
    assert dashboard_info["lunar_two"]["features"] == 11
    assert dashboard_info["lunar_two"]["landing_sites"] == 16
    assert dashboard_info["lunar_two"]["altitudes"] == 0
