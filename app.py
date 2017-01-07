import os

from flask import Flask, json, request

from helpers import get_moon_info

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "This is a web service. Nothing to see here!"

@app.route('/moon_info')
def moon_info():
    date = float(request.args.get('date', 0))
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))

    json_str = json.dumps(get_moon_info(date, lat, lon))
    return json_str


if __name__ == "__main__":
    app.run()
