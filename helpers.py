from datetime import datetime
import math

from pylunar import MoonInfo

def convert_dec_loc_to_loc_tuple(loc):
    degrees = int(loc)
    minutes = math.fabs((loc - degrees)) * 60.0
    seconds = (minutes - round(minutes)) * 60.0
    return (degrees, round(minutes), round(seconds))

def get_moon_info(date, lat, lon):
    d = datetime.fromtimestamp(date)
    date_tuple = (d.year, d.month, d.day, d.hour, d.minute, d.second)
    lat_tuple = convert_dec_loc_to_loc_tuple(lat)
    lon_tuple = convert_dec_loc_to_loc_tuple(lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)
    #print(moon_info.observer)
    phase_name = " ".join(moon_info.phase_name().split('_')).title()

    next_four_phases = {str(i): {"phase": phases[0], "datetime": phases[1]}
                        for i, phases in enumerate(moon_info.next_four_phases())}

    return {"age": moon_info.age(), "colong": moon_info.colong(),
            "fractional_phase": moon_info.fractional_phase(), "libration_lon": moon_info.libration_lon(),
            "libration_lat": moon_info.libration_lat(), "altitude": moon_info.altitude(),
            "azimuth": moon_info.azimuth(), "phase": phase_name,
            "next_four_phases": next_four_phases}
