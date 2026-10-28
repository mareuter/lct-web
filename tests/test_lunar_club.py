# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Tests for lunar_club routes."""

from __future__ import annotations

from fastapi.testclient import TestClient

from lct_web.main import app

client = TestClient(app)


def test_lunar_club() -> None:
    response = client.get(
        "/lunar_club", params={"date": 1382133600.0, "lat": 35.9694444444444, "lon": -84.316666666666}
    )
    assert response.status_code == 200

    lunar_club_info = response.json()
    assert lunar_club_info["time_events"]["time_from_new"] is None
    assert lunar_club_info["time_events"]["time_to_new"] is None
    assert not lunar_club_info["time_events"]["cresent_moon_waxing"]
    assert not lunar_club_info["time_events"]["old_moon_in_new_moons_arms"]
    assert not lunar_club_info["time_events"]["cresent_moon_waning"]
    assert not lunar_club_info["time_events"]["new_moon_in_old_moon_arms"]
    assert not lunar_club_info["phase_events"]["cow_jumping_over_the_moon"]
    assert lunar_club_info["phase_events"]["man_in_the_moon"]
    assert lunar_club_info["phase_events"]["woman_in_the_moon"]
    assert lunar_club_info["phase_events"]["rabbit_in_the_moon"]
    assert len(lunar_club_info["naked_eye_features"]) == 10
    assert len(lunar_club_info["binocular_features"]) == 2
    assert len(lunar_club_info["telescope_features"]) == 0
