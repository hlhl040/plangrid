import app
import unittest
import requests
import json
import sys

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_post(self):
        response = self.app.post('/')
        self.assertEqual(response.data, "POST Request")

    def test_get_with_right_header(self):
    	headers = {'Accept': 'application/json'}
    	response = self.app.get('/', headers=headers)
    	self.assertEqual(response.data, '{"message": "Good morning"}')

    def test_get_with_wrong_header(self):
    	headers = {'Accept': 'xxx'}
    	response = self.app.get('/', headers=headers)
    	self.assertEqual(response.data, 'Accept header not set to application/json')

    def test_get_without_Accept_header(self):
    	headers = None
    	response = self.app.get('/', headers=headers)
    	self.assertEqual(response.data, '<p>Hello, World</p>')


if __name__ == "__main__":
    unittest.main()