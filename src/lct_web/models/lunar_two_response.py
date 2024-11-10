# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for lunar_two route."""

from __future__ import annotations

from pydantic import BaseModel

from ..pkg_types import AltitudeDict, FeatureDict

__all__ = ["LunarTwoResponse"]


class LunarTwoResponse(BaseModel):
    """Response model for the lunar_two route."""

    features: FeatureDict
    landing_sites: FeatureDict
    altitudes: AltitudeDict
