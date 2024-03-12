# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Tests for API routes."""

from __future__ import annotations

import os

from fastapi.testclient import TestClient
from lct_web.main import app
from pydantic import ValidationError
import pytest

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "This is a web service, nothing to see here."}


def test_bad_location() -> None:
    with pytest.raises(ValidationError) as err:
        client.get(
            "/moon_info",
            params={
                "lat": 96.5,
                "lon": 184.342,
                "date": 1677880560.0,
                "timezone": "Madeup/Honalee",
            },
        )
    lines = str(err).split(os.linesep)
    assert "3 validation errors for DateLoc" in lines[0]
    for i, line in enumerate(lines):
        if line.startswith("lat"):
            assert "Input should be less than or equal to 90" in lines[i + 1]
        if line.startswith("lon"):
            assert "Input should be less than or equal to 180" in lines[i + 1]
        if line.startswith("timezone"):
            assert "Unknown timezone" in lines[i + 1]
