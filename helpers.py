from datetime import datetime

from pylunar import MoonInfo

def convert_dec_loc_to_loc_tuple(loc):
    degrees = int(loc)
    minutes = int((loc - degrees) * 60.0)
    seconds = int((loc - degrees) * 3600.0)
    return (degrees, minutes, seconds)

def get_moon_info(date, lat, lon):
    d = datetime.fromtimestamp(date)
    date_tuple = (d.year, d.month, d.day, d.hour, d.minute, d.second)
    lat_tuple = convert_dec_loc_to_loc_tuple(lat)
    lon_tuple = convert_dec_loc_to_loc_tuple(lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)

    return {"age": moon_info.age()}
