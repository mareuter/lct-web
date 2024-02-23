# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Module for defining package types."""

from __future__ import annotations

from pylunar.types import DateTimeTuple, LunarFeatureList

__all__ = ["NextFourPhases", "RiseSetTimes"]

FeatureDict = dict[str, LunarFeatureList]
NextFourPhases = dict[str, dict[str, str | DateTimeTuple]]
RiseSetTimes = dict[str, dict[str, str | DateTimeTuple]]