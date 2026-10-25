# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for features route."""

from __future__ import annotations

from pydantic import BaseModel

from ..pkg_types import FeaturesDict

__all__ = ["FeatureResponse", "FeaturesResponse"]


class FeaturesResponse(BaseModel):
    """Response model for the features route."""

    features: FeaturesDict


class FeatureResponse(BaseModel):
    """Response model for the feature route."""

    pass
