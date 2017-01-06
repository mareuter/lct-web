from flask import json, url_for

from app import app

class TestApp(object):

    def setup_class(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_basic_content(self):
        response = self.client.get('/')
        assert response.data == b'Hello World!'
        assert response.status_code == 200

    def test_moon_info(self):
        with app.test_request_context():
            moon_info_url = url_for("moon_info", date=1382158800.0, lat=35.9694444444444,
                                    lon=-84.316666666666)
            response = self.client.get(moon_info_url)
            moon_info = json.loads(response.data)
            assert response.status_code == 200
            assert moon_info["age"] == 13.892695861570246
            assert moon_info["colong"] == 83.97189956624061
            assert moon_info["fractional_phase"] == 0.9998519924481626
            assert moon_info["libration_lon"] == 5.23107551788429
            assert moon_info["libration_lat"] == -1.4788210646482465
            assert moon_info["altitude"] == -9.8149186580585
            assert moon_info["azimuth"] == 69.75156520051686
            next_four_phases = moon_info["next_four_phases"]
            assert len(next_four_phases) == 4
            assert next_four_phases[0][0] == "full"
            assert next_four_phases[0][1] == [2013, 10, 18, 23, 37, 39.644067962653935]
