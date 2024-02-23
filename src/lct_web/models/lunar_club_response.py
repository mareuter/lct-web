# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

from pydantic import BaseModel

from ..pkg_types import FeatureDict

__all__ = ["LunarClubResponse"]

class LunarClubResponse(BaseModel):
    time_from_new_moon: float
    time_to_new_moon: float
    time_to_full_moon: float
    fractional_phase: float
    naked_eye_features: FeatureDict
    binocular_features: FeatureDict
    telescope_features: FeatureDict
