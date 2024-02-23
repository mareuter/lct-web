# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Routing definitions for moon_info."""

from fastapi import APIRouter
from pylunar import MoonInfo

from ..dependencies import DateLocDeps
from ..helpers import format_date_and_location
from ..models.moon_info_response import MoonInfoResponse

__all__ = ["router"]

router = APIRouter()

@router.get("/moon_info")
def moon_info(params: DateLocDeps) -> MoonInfoResponse:
    date = params.date
    timezone = params.timezone
    lat = params.lat
    lon = params.lon

    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)
    # print(moon_info.observer.date)
    phase_name = " ".join(moon_info.phase_name().split('_')).title()

    next_four_phases = {str(i): {"phase": phases[0], "datetime": phases[1]}
                        for i, phases in enumerate(moon_info.next_four_phases())}

    rise_set_times = {str(i): {"time": times[0], "datetime": times[1]}
                      for i, times in enumerate(moon_info.rise_set_times(timezone))}

    return MoonInfoResponse(age=moon_info.age(), colong=moon_info.colong(),
            fractional_phase=moon_info.fractional_phase(), libration_lon=moon_info.libration_lon(),
            libration_lat=moon_info.libration_lat(),
            libration_phase_angle=moon_info.libration_phase_angle(), altitude=moon_info.altitude(),
            azimuth=moon_info.azimuth(), ra=moon_info.ra(), dec=moon_info.dec(),
            magnitude=moon_info.magnitude(), earth_distance=moon_info.earth_distance(),
            subsolar_lat=moon_info.subsolar_lat(), angular_size=moon_info.angular_size(),
            elongation=moon_info.elongation(), phase=phase_name,
            next_four_phases=next_four_phases, rise_set_times=rise_set_times)
