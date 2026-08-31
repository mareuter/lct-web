# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for altitude events in Lunar II Club."""

from __future__ import annotations

from pydantic import BaseModel

__all__ = ["AltitudeEvents"]


class AltitudeEvents(BaseModel):
    """Model for altitude events in Lunar II Club."""

    events: list[tuple[str, int | None, float]]

    def isActive(self) -> bool:
        """Determine if any of the altitude events are active.

        Returns
        -------
        bool
            True is at least one event is active, False if not.
        """
        is_active = False
        for event in self.events:
            is_active = event[1] is not None
        return is_active
