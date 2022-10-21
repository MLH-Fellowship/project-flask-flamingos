# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        print('set_up_done')

    def test_home(self):
        print('test_home')
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        print(html)
        assert "<title></title>" in html
        # TODO Add more tests relating to the home page

    def test_timeline(self):
        print('test_timeline')
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json