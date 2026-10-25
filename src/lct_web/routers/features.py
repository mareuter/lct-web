# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Routing definitions for features."""

from collections import OrderedDict, defaultdict
from enum import StrEnum

from fastapi import APIRouter
from pylunar import LunarFeatureContainer

from ..models.features_response import FeaturesResponse
from ..pkg_types import FeaturesDict

__all__ = ["router"]


class ClubType(StrEnum):
    lunar = "Lunar"
    lunar2 = "LunarII"


router = APIRouter()


@router.get("/features/{club_type}")
def features(club_type: ClubType) -> FeaturesResponse:
    lfc = LunarFeatureContainer(club_type.value)
    lfc.load(None)

    temp: FeaturesDict = defaultdict(list)
    for i, feature in enumerate(lfc):
        temp[feature.feature_type].append((i, feature.name))

    features: FeaturesDict = OrderedDict()
    for key in sorted(temp):
        features[key] = sorted(temp[key])

    return FeaturesResponse(features=features)
