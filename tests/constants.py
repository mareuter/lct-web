# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Constants used for testing."""

DATE_LOC_PARAMS = {
    "date": 1382133600.0,
    "lat": 35.9694444444444,
    "lon": -84.316666666666,
}
"""Date and location data."""

DATE_LOC_TZ_PARAMS = {**DATE_LOC_PARAMS, "timezone": "America/New_York"}
"""Date, location and timezone data."""
