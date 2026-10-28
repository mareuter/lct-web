# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Routing definitions for lunar_club."""

from __future__ import annotations

from fastapi import APIRouter
from pylunar import LunarFeatureContainer, MoonInfo

from ..club_logic import check_full_moon_events, check_new_moon_events
from ..dependencies import DateLocDeps
from ..helpers import format_date_and_location
from ..models.lunar_club_response import LunarClubResponse

__all__ = ["router"]

router = APIRouter()


@router.get("/lunar_club")
def lunar_club(params: DateLocDeps) -> LunarClubResponse:
    date = params.date
    lat = params.lat
    lon = params.lon

    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)

    phase_events = check_full_moon_events(moon_info.time_to_full_moon(), moon_info.fractional_phase())
    time_events = check_new_moon_events(moon_info.time_from_new_moon(), moon_info.time_to_new_moon())

    lfc = LunarFeatureContainer("Lunar")
    lfc.load(moon_info)

    nef = []
    bf = []
    tf = []
    for i, feature in enumerate(lfc):
        if feature.lunar_club_type == "Naked Eye":
            nef.append((i, feature.name))
        if feature.lunar_club_type == "Binocular":
            bf.append((i, feature.name))
        if feature.lunar_club_type == "Telescopic":
            tf.append((i, feature.name))

    return LunarClubResponse(
        time_events=time_events,
        phase_events=phase_events,
        naked_eye_features=nef,
        binocular_features=bf,
        telescope_features=tf,
    )
