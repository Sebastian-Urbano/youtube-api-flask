# try:
from app import application
import unittest
import json
from os import getenv
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = getenv('YOUTUBE_API_KEY')


class YoutubeTest(unittest.TestCase):
    # check for response status

    def test_status_code(self):
        query = json.dumps(
            {"query": "youtube-api", "YOUTUBE_API_KEY": YOUTUBE_API_KEY})
        self.tester = application.test_client(self)
        self.response = self.tester.post(
            "/youtube-search", headers={"Content-Type": "application/json"}, data=query)
        self.statuscode = self.response.status_code
        self.assertEqual(200, self.statuscode)

    # check if the content return is application/json
    def test_content_return(self):
        query = json.dumps(
            {"query": "youtube-api", "YOUTUBE_API_KEY": YOUTUBE_API_KEY})
        self.tester = application.test_client(self)
        self.response = self.tester.post(
            "/youtube-search", headers={"Content-Type": "application/json"}, data=query)
        self.assertEqual(self.response.content_type, "application/json")

    # check for the response, as we need that the answer has description, image_url and title
    def test_description_response(self):
        query = json.dumps(
            {"query": "youtube-api", "YOUTUBE_API_KEY": YOUTUBE_API_KEY})
        self.tester = application.test_client(self)
        self.response = self.tester.post(
            "/youtube-search", headers={"Content-Type": "application/json"}, data=query)
        self.assertTrue(b'description' in self.response.data)

    def test_title_response(self):
        query = json.dumps(
            {"query": "youtube-api", "YOUTUBE_API_KEY": YOUTUBE_API_KEY})
        self.tester = application.test_client(self)
        self.response = self.tester.post(
            "/youtube-search", headers={"Content-Type": "application/json"}, data=query)
        self.assertTrue(b'title' in self.response.data)

    def test_image_url_response(self):
        query = json.dumps(
            {"query": "youtube-api", "YOUTUBE_API_KEY": YOUTUBE_API_KEY})
        self.tester = application.test_client(self)
        self.response = self.tester.post(
            "/youtube-search", headers={"Content-Type": "application/json"}, data=query)
        self.assertTrue(b'image_url' in self.response.data)


if __name__ == "__main__":
    unittest.main()
