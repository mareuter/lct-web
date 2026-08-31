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
from pylunar import AltitudeDict, LunarFeatureContainer

from ..club_logic import check_altitude_events, check_full_moon_events, check_new_moon_events
from ..dependencies import DateLocDeps
from ..helpers import create_moon_info
from ..models.dashboard_response import DashboardResponse
from ..models.phase_info import PhaseInfo
from ..models.summaries import LunarClub, LunarTwo

__all__ = ["router"]

router = APIRouter()


@router.get("/dashboard")
def dashboard(params: DateLocDeps) -> DashboardResponse:
    moon_info = create_moon_info(params)
    phase_name = " ".join(moon_info.phase_name().split("_")).title()
    next_four_phases = moon_info.next_four_phases()
    next_phase = next_four_phases[0]

    phase_events = check_full_moon_events(moon_info.time_to_full_moon(), moon_info.fractional_phase())
    time_events = check_new_moon_events(moon_info.time_from_new_moon(), moon_info.time_to_new_moon())

    lfc1 = LunarFeatureContainer("Lunar")
    lfc1.load(moon_info)
    lc_ne = 0
    lc_bino = 0
    lc_tel = 0
    for feature in lfc1:
        if feature.lunar_club_type == "Naked Eye":
            lc_ne += 1
        if feature.lunar_club_type == "Binocular":
            lc_bino += 1
        if feature.lunar_club_type == "Telescope":
            lc_tel += 1

    lfc2 = LunarFeatureContainer("LunarII")
    lfc2.load(moon_info)

    l2_feat = 0
    l2_ls = 0
    for feature in lfc2:
        if feature.feature_type == "Landing Site":
            l2_ls += 1
        else:
            l2_feat += 1

    ad = AltitudeDict()
    ad.load(moon_info)
    alt_events = check_altitude_events(ad)

    return DashboardResponse(
        age=moon_info.age(),
        altitude=moon_info.altitude(),
        azimuth=moon_info.azimuth(),
        colong=moon_info.colong(),
        fractional_phase=moon_info.fractional_phase(),
        phase=phase_name,
        next_phase=[PhaseInfo(id=0, phase=next_phase[0], datetime=next_phase[1])],
        lunar_club=LunarClub(
            time_events=time_events.isActive(),
            phase_events=phase_events.isActive(),
            naked_eye=lc_ne,
            binocular=lc_bino,
            telescope=lc_tel,
        ),
        lunar_two=LunarTwo(features=l2_feat, landing_sites=l2_ls, altitude_events=alt_events.isActive()),
    )
