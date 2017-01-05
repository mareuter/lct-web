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
            moon_info_url = url_for("moon_info", date=1382158800.0, lat=-84.316666666666,
                                    lon=35.9694444444444)
            response = self.client.get(moon_info_url)
            moon_info = json.loads(response.data)
            assert response.status_code == 200
            assert moon_info["age"] == 13.892695861570246
