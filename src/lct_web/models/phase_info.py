# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Model for phase information."""

from __future__ import annotations

from pydantic import BaseModel
from pylunar.pkg_types import DateTimeTuple

__all__ = ["PhaseInfo"]


class PhaseInfo(BaseModel):
    """Model for phase information."""

    id: int
    phase: str
    datetime: DateTimeTuple
