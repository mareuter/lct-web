# This file is part of lct-web.
#
# Developed by Michael Reuter.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

"""Functions to apply observing club logic to set information."""

from __future__ import annotations

from .models.special_events import PhaseEvents, TimeEvents

__all__ = ["check_full_moon_events", "check_new_moon_events"]


def check_full_moon_events(time_to_full: float, fractional_phase: float) -> PhaseEvents:
    """Determine if any of the Lunar Club phase events are active.

    Parameters
    ----------
    time_to_full : float
        Time in hours to the full moon.
    fractional_phase : float
        The fractional phase of the moon.

    Returns
    -------
    PhaseEvents
        The special phase event information.
    """
    time_cow_jumping = [2.0, 3.0]
    full_moon_fraction = 0.987

    phase_events = PhaseEvents()

    if time_to_full >= time_cow_jumping[0] and time_to_full <= time_cow_jumping[1]:
        phase_events.cow_jumping_over_the_moon = True

    if fractional_phase >= full_moon_fraction:
        phase_events.man_in_the_moon = True
        phase_events.woman_in_the_moon = True
        phase_events.rabbit_in_the_moon = True

    return phase_events


def check_moon_time(moon_time: float, cutoff_time: float, phase_time: float) -> tuple[bool, int]:
    """Determine information for the time events.

    Parameters
    ----------
    moon_time : float
        The time of the moon in hours.
    cutoff_time : float
        Cutoff time for the time event.
    phase_time : float
        Break point for the different time events.

    Returns
    -------
    tuple[bool, int]
        time_is_active: If the time event is active
        indicator_state: Which if the phases the time event is in.
    """
    time_is_active = False
    indicator_state = 0

    if moon_time <= cutoff_time:
        time_is_active = True
        indicator_state = 2 if moon_time > phase_time else 1

    return (time_is_active, indicator_state)


def check_new_moon_events(time_from_new: float, time_to_new: float) -> TimeEvents:
    """Determine if any of the Lunar Club time events are active.

    Parameters
    ----------
    time_from_new : float
        Time in hours from the new moon.
    time_to_new : float
        Time in hours to the new moon.

    Returns
    -------
    TimeEvents
        The time event information.
    """
    time_cutoff = 72.0
    time_waxing_cresent = 40.0
    time_waning_cresent = 48.0

    time_from_new_active, from_new_indicator = check_moon_time(
        time_from_new, time_cutoff, time_waxing_cresent
    )
    time_to_new_active, to_new_indicator = check_moon_time(time_to_new, time_cutoff, time_waning_cresent)

    time_events = TimeEvents(
        time_from_new=time_from_new if time_from_new_active else None,
        time_to_new=time_to_new if time_to_new_active else None,
        cresent_moon_waxing=from_new_indicator == 1,
        old_moon_in_new_moons_arms=from_new_indicator == 2,
        cresent_moon_waning=to_new_indicator == 1,
        new_moon_in_old_moon_arms=to_new_indicator == 2,
    )

    return time_events
