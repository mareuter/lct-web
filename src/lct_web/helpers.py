# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Common functions for routes."""

from __future__ import annotations

from datetime import datetime, UTC
import math

from pylunar.pkg_types import DateTimeTuple, DmsCoordinate

__all__ = ["check_for_bad_lat_lon", "convert_dec_loc_to_loc_tuple", "format_date_and_location"]


def check_for_bad_lat_lon(lat: float, lon: float) -> bool:
    """Check for latitude and longitude out of range.

    Parameters
    ----------
    lat : float
        The latitude to check.
    lon : float
        The longitude to check.

    Returns
    -------
    bool
        True if values are in range, False if not.
    """
    return lat > math.fabs(90.0) or lon > math.fabs(180.0)


def convert_dec_loc_to_loc_tuple(loc: float) -> DmsCoordinate:
    """Convert decimal lat/lon to integer tuple.

    Parameters
    ----------
    loc : float
        The location coordinate in decimal degrees.

    Returns
    -------
    DmsCoordinate
        The DMS coordinate from the given input location.
    """
    degrees = int(loc)
    minutes = math.fabs(loc - degrees) * 60.0
    seconds = (minutes - round(minutes)) * 60.0
    return (degrees, round(minutes), round(seconds))


def format_date_and_location(
    date: float, lat: float, lon: float
) -> tuple[DateTimeTuple, DmsCoordinate, DmsCoordinate]:
    """Format the date and location coordinates into pylunar quantities.

    Parameters
    ----------
    date : float
        The decimal date (a UNIX timestamp).
    lat : float
        The latitude of the location in decimal decgrees.
    lon : float
        The longitude of the location in decimal degrees.

    Returns
    -------
    tuple[DateTimeTuple, DmsCoordinate, DmsCoordinate]
        The formatted quantities.
    """
    d = datetime.fromtimestamp(date, UTC)
    date_tuple = (d.year, d.month, d.day, d.hour, d.minute, d.second)
    lat_tuple = convert_dec_loc_to_loc_tuple(lat)
    lon_tuple = convert_dec_loc_to_loc_tuple(lon)
    return date_tuple, lat_tuple, lon_tuple
