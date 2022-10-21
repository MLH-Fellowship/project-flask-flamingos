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

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html