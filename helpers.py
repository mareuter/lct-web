from datetime import datetime
import math

from pylunar import LunarFeatureContainer, MoonInfo

def convert_dec_loc_to_loc_tuple(loc):
    degrees = int(loc)
    minutes = math.fabs((loc - degrees)) * 60.0
    seconds = (minutes - round(minutes)) * 60.0
    return (degrees, round(minutes), round(seconds))

def format_date_and_location(date, lat, lon):
    d = datetime.utcfromtimestamp(date)
    date_tuple = (d.year, d.month, d.day, d.hour, d.minute, d.second)
    lat_tuple = convert_dec_loc_to_loc_tuple(lat)
    lon_tuple = convert_dec_loc_to_loc_tuple(lon)
    return date_tuple, lat_tuple, lon_tuple

def get_moon_info(date, timezone, lat, lon):
    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)
    #print(moon_info.observer.date)
    phase_name = " ".join(moon_info.phase_name().split('_')).title()

    next_four_phases = {str(i): {"phase": phases[0], "datetime": phases[1]}
                        for i, phases in enumerate(moon_info.next_four_phases())}

    rise_set_times = {str(i): {"time": times[0], "datetime": times[1]}
                      for i, times in enumerate(moon_info.rise_set_times(timezone))}
    # REMOVE when this is called in above function
    moon_info.update(date_tuple)

    return {"age": moon_info.age(), "colong": moon_info.colong(),
            "fractional_phase": moon_info.fractional_phase(), "libration_lon": moon_info.libration_lon(),
            "libration_lat": moon_info.libration_lat(), "altitude": moon_info.altitude(),
            "azimuth": moon_info.azimuth(), "ra": moon_info.ra(), "dec": moon_info.dec(),
            "magnitude": moon_info.magnitude(), "earth_distance": moon_info.earth_distance(),
            "subsolar_lat": moon_info.subsolar_lat(), "angular_size": moon_info.angular_size(),
            "elongation": moon_info.elongation(), "phase": phase_name,
            "next_four_phases": next_four_phases, "rise_set_times": rise_set_times}

def get_lunar_club_info(date, lat, lon):
    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)

    lfc = LunarFeatureContainer("Lunar")
    lfc.load(moon_info)

    nef = {}
    bf = {}
    tf = {}
    for i, feature in enumerate(lfc):
        if feature.lunar_club_type == "Naked Eye":
            nef[str(i)] = list_from_feature(feature)
        if feature.lunar_club_type == "Binocular":
            bf[str(i)] = list_from_feature(feature)
        if feature.lunar_club_type == "Telescopic":
            tf[str(i)] = list_from_feature(feature)

    return {"time_from_new_moon": moon_info.time_from_new_moon(),
            "time_to_new_moon": moon_info.time_to_new_moon(),
            "time_to_full_moon": moon_info.time_to_full_moon(),
            "fractional_phase": moon_info.fractional_phase(),
            "naked_eye_features": nef,
            "binocular_features": bf,
            "telescope_features": tf}

def get_lunar_two_info(date, lat, lon):
    date_tuple, lat_tuple, lon_tuple = format_date_and_location(date, lat, lon)

    moon_info = MoonInfo(lat_tuple, lon_tuple)
    moon_info.update(date_tuple)

    lfc = LunarFeatureContainer("LunarII")
    lfc.load(moon_info)

    features = {}
    for i, feature in enumerate(lfc):
        features[str(i)] = list_from_feature(feature)

    return {"features": features}

def list_from_feature(feature):
    fl = [feature.name, feature.latitude, feature.longitude, feature.feature_type,
          feature.delta_latitude, feature.delta_longitude]
    return fl
