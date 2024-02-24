# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Dependencies for routes."""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends

from .models.dateloc import DateLoc

__all__ = ["DateLocDeps"]


def dateloc_parameters(date: float = 0, timezone: str = "UTC", lat: float = 0, lon: float = 0) -> DateLoc:
    return DateLoc(date=date, timezone=timezone, lat=lat, lon=lon)


DateLocDeps = Annotated[DateLoc, Depends(dateloc_parameters)]
