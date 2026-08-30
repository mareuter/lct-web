# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Routing definition for dashboard."""

from fastapi import APIRouter

from ..dependencies import DateLocDeps
from ..helpers import create_moon_info
from ..models.dashboard_response import DashboardResponse
from ..models.phase_info import PhaseInfo

__all__ = ["router"]

router = APIRouter()


@router.get("/dashboard")
def dashboard(params: DateLocDeps) -> DashboardResponse:
    moon_info = create_moon_info(params)
    phase_name = " ".join(moon_info.phase_name().split("_")).title()
    next_four_phases = moon_info.next_four_phases()
    next_phase = next_four_phases[0]

    return DashboardResponse(
        age=moon_info.age(),
        altitude=moon_info.altitude(),
        azimuth=moon_info.azimuth(),
        colong=moon_info.colong(),
        fractional_phase=moon_info.fractional_phase(),
        phase=phase_name,
        next_phase=[PhaseInfo(id=0, phase=next_phase[0], datetime=next_phase[1])],
    )
