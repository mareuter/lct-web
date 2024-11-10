# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Routing definitions for lunar_two."""

from __future__ import annotations

from fastapi import APIRouter
from pylunar import AltitudeDict, LunarFeatureContainer, MoonInfo

from ..dependencies import DateLocDeps
from ..helpers import format_date_and_location
from ..models.lunar_two_response import LunarTwoResponse

__all__ = ["router"]

router = APIRouter()


@router.get("/lunar_two")
def lunar_two(params: DateLocDeps) -> LunarTwoResponse:
    date = params.date
    lat = params.lat
    lon = params.lon

    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)

    lfc = LunarFeatureContainer("LunarII")
    lfc.load(moon_info)

    ad = AltitudeDict()
    ad.load(moon_info)

    features = {}
    landing_sites = {}
    for i, feature in enumerate(lfc):
        if feature.feature_type == "Landing Site":
            landing_sites[str(i)] = feature.list_from_feature()
        else:
            features[str(i)] = feature.list_from_feature()

    return LunarTwoResponse(features=features, landing_sites=landing_sites, altitudes=ad)
