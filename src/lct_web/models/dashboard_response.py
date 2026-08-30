# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for dashboard route."""

from __future__ import annotations

from pydantic import BaseModel

from .phase_info import PhaseInfo

__all__ = ["DashboardResponse"]


class DashboardResponse(BaseModel):
    """Response model for the dashboard route."""

    age: float
    altitude: float
    azimuth: float
    colong: float
    fractional_phase: float
    phase: str
    next_phase: list[PhaseInfo]
