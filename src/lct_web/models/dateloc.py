# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for query parameters."""

from __future__ import annotations

from math import fabs
import zoneinfo

from fastapi import Query
from pydantic import BaseModel, field_validator

__all__ = ["DateLoc"]


class DateLoc(BaseModel):
    """Model for route query parameters."""

    date: float = Query(0, title="Date", description="A UNIX timestamp holding the requested date.")
    timezone: str = Query("UTC", title="Timezone", description="The timezone for the given location.")
    lat: float = Query(0, title="Latitude", description="The latitude for the given location.", le=fabs(90.0))
    lon: float = Query(
        0, title="Longitude", description="The longitude for the given location.", le=fabs(180.0)
    )

    @field_validator("timezone")
    @classmethod
    def check_timezone(cls, tz: str) -> str:
        """Check for timezone name."""
        try:
            zoneinfo.ZoneInfo(tz)
        except zoneinfo.ZoneInfoNotFoundError:
            raise ValueError(f"Unknown timezone {tz}") from None
        return tz
