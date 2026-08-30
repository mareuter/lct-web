# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Models for time and phase events in Lunar Club."""

from __future__ import annotations

from pydantic import BaseModel

__all__ = ["PhaseEvents", "TimeEvents"]


class PhaseEvents(BaseModel):
    """Model for phase events in Lunar Club."""

    cow_jumping_over_the_moon: bool = False
    man_in_the_moon: bool = False
    woman_in_the_moon: bool = False
    rabbit_in_the_moon: bool = False

    def isActive(self) -> bool:
        """Determine if any phase events are active.

        Returns
        -------
        bool
            True if any phase events are active, False otherwise.
        """
        return (
            self.cow_jumping_over_the_moon
            or self.man_in_the_moon
            or self.woman_in_the_moon
            or self.rabbit_in_the_moon
        )


class TimeEvents(BaseModel):
    """Model for time events in Lunar Club."""

    time_from_new: float | None
    time_to_new: float | None
    cresent_moon_waxing: bool = False
    old_moon_in_new_moons_arms: bool = False
    cresent_moon_waning: bool = False
    new_moon_in_old_moon_arms: bool = False

    def isActive(self) -> bool:
        """Determine if any time events are active.

        Returns
        -------
        bool
            True if any time events are active, False otherwise.
        """
        return (
            self.cresent_moon_waxing
            or self.old_moon_in_new_moons_arms
            or self.cresent_moon_waning
            or self.new_moon_in_old_moon_arms
        )
