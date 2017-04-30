from flask import json, url_for

from app import app

class TestApp(object):

    def setup_class(self):
        self.client = app.test_client()
        self.client.testing = True
        self.date = 1382133600.0
        self.latitude = 35.9694444444444
        self.longitude = -84.316666666666

    def test_basic_content(self):
        response = self.client.get('/')
        assert response.data == b'This is a web service. Nothing to see here!'
        assert response.status_code == 200

    def test_moon_info(self):
        with app.test_request_context():
            moon_info_url = url_for("moon_info", date=self.date, lat=self.latitude,
                                    lon=self.longitude)
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
            assert moon_info["phase"] == "Full Moon"
            next_four_phases = moon_info["next_four_phases"]
            assert len(next_four_phases) == 4
            assert next_four_phases["0"]["phase"] == "full_moon"
            assert next_four_phases["0"]["datetime"] == [2013, 10, 18, 23, 37, 39.644067962653935]

    def test_lunar_club_info(self):
        with app.test_request_context():
            lunar_club_info_url = url_for("lunar_club", date=self.date, lat=self.latitude,
                                          lon=self.longitude)
            response = self.client.get(lunar_club_info_url)
            lunar_club_info = json.loads(response.data)
            assert response.status_code == 200
            assert lunar_club_info["time_from_new_moon"] == 333.4247006776859
            assert lunar_club_info["time_to_new_moon"] == 374.8327396878158
            assert lunar_club_info["time_to_full_moon"] == 0.06781995449273381
            assert lunar_club_info["fractional_phase"] == 0.9998519924481626
