# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

from pydantic import BaseModel

from ..pkg_types import NextFourPhases, RiseSetTimes

__all__ = ["MoonInfoResponse"]

class MoonInfoResponse(BaseModel):
    age: float
    colong: float
    fractional_phase: float
    libration_lon: float
    libration_lat: float
    libration_phase_angle: float
    altitude: float
    azimuth: float
    ra: float
    dec: float
    magnitude: float
    earth_distance: float
    subsolar_lat: float
    angular_size: float
    elongation: float
    phase: str
    next_four_phases: NextFourPhases
    rise_set_times: RiseSetTimes