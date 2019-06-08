import os

from flask import Flask, json, request
from flask_cors import CORS, cross_origin

from helpers import get_moon_info, get_lunar_club_info, get_lunar_two_info
from helpers import BadCoordinatesGiven, check_for_bad_lat_lon

app = Flask(__name__)
cors = CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    return "This is a web service. Nothing to see here!"


@app.route('/moon_info')
@cross_origin()
def moon_info():
    date = float(request.args.get('date', 0))
    timezone = str(request.args.get('tz', 'UTC'))
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))

    if check_for_bad_lat_lon(lat, lon):
        raise BadCoordinatesGiven

    json_str = json.dumps(get_moon_info(date, timezone, lat, lon))
    return json_str


@app.route('/lunar_club')
def lunar_club():
    date = float(request.args.get('date', 0))
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))

    if check_for_bad_lat_lon(lat, lon):
        raise BadCoordinatesGiven

    json_str = json.dumps(get_lunar_club_info(date, lat, lon))
    return json_str


@app.route('/lunar_two')
def lunar_two():
    date = float(request.args.get('date', 0))
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))

    if check_for_bad_lat_lon(lat, lon):
        raise BadCoordinatesGiven

    json_str = json.dumps(get_lunar_two_info(date, lat, lon))
    return json_str


@app.errorhandler(BadCoordinatesGiven)
def handle_bad_request(e):
    return "Bad coordinates given.", 400


if __name__ == "__main__":
    app.run()
