# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Models for club summary information."""

from __future__ import annotations

from pydantic import BaseModel

__all__ = ["LunarClub", "LunarTwo"]


class LunarClub(BaseModel):
    """Model for Lunar Club summary information."""

    time_events: bool
    phase_events: bool
    naked_eye: int
    binocular: int
    telescope: int


class LunarTwo(BaseModel):
    """Model for Lunar II Club summary information."""

    features: int
    landing_sites: int
    altitude_events: bool = False
