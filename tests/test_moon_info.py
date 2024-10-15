# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Tests for moon_info routes."""

from __future__ import annotations

from fastapi.testclient import TestClient

from lct_web.main import app

client = TestClient(app)


def test_moon_info() -> None:
    response = client.get(
        "/moon_info",
        params={
            "date": 1382133600.0,
            "timezone": "America/New_York",
            "lat": 35.9694444444444,
            "lon": -84.316666666666,
        },
    )
    assert response.status_code == 200
    moon_info = response.json()
    assert moon_info["age"] == 13.892695999260468
    assert moon_info["colong"] == 83.97189956624061
    assert moon_info["fractional_phase"] == 0.9998519924481626
    assert moon_info["libration_lon"] == 5.23107551788429
    assert moon_info["libration_lat"] == -1.4788210646482465
    assert moon_info["libration_phase_angle"] == 105.7855572234932
    assert moon_info["altitude"] == -9.814919511832146
    assert moon_info["azimuth"] == 69.75156520051686
    assert moon_info["phase"] == "Full Moon"
    next_four_phases = moon_info["next_four_phases"]
    assert len(next_four_phases) == 4
    assert next_four_phases["0"]["phase"] == "full_moon"
    assert next_four_phases["0"]["datetime"] == [2013, 10, 18, 23, 37, 39.633078]
    assert moon_info["magnitude"] == -12.63
    assert moon_info["earth_distance"] == 386484.25078267464
    assert moon_info["ra"] == 23.331890450649784
    assert moon_info["dec"] == 10.129795616523591
    assert moon_info["angular_size"] == 0.5159071519639757
    assert moon_info["subsolar_lat"] == -0.3366501792590513
    assert moon_info["elongation"] == 178.56298828125
    assert moon_info["rise_set_times"]["0"]["time"] == "transit"
    assert moon_info["rise_set_times"]["0"]["datetime"] == [2013, 10, 18, 0, 43, 21]
    assert moon_info["rise_set_times"]["1"]["time"] == "set"
    assert moon_info["rise_set_times"]["1"]["datetime"] == [2013, 10, 18, 7, 22, 18]
    assert moon_info["rise_set_times"]["2"]["time"] == "rise"
    assert moon_info["rise_set_times"]["2"]["datetime"] == [2013, 10, 18, 18, 47, 40]
