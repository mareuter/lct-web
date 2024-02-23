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

    lfc = LunarFeatureContainer("Lunar")
    lfc.load(moon_info)

    nef = {}
    bf = {}
    tf = {}
    for i, feature in enumerate(lfc):
        if feature.lunar_club_type == "Naked Eye":
            nef[str(i)] = feature.list_from_feature()
        if feature.lunar_club_type == "Binocular":
            bf[str(i)] = feature.list_from_feature()
        if feature.lunar_club_type == "Telescopic":
            tf[str(i)] = feature.list_from_feature()

    return LunarClubResponse(
        time_from_new_moon=moon_info.time_from_new_moon(),
        time_to_new_moon=moon_info.time_to_new_moon(),
        time_to_full_moon=moon_info.time_to_full_moon(),
        fractional_phase=moon_info.fractional_phase(),
        naked_eye_features=nef,
        binocular_features=bf,
        telescope_features=tf,
    )
