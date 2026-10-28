# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for lunar_club route."""

from __future__ import annotations

from pydantic import BaseModel

from ..models.special_events import PhaseEvents, TimeEvents
from ..pkg_types import FeatureList

__all__ = ["LunarClubResponse"]


class LunarClubResponse(BaseModel):
    """Response model for the lunar_club route."""

    time_events: TimeEvents
    phase_events: PhaseEvents
    naked_eye_features: FeatureList
    binocular_features: FeatureList
    telescope_features: FeatureList
