from flask import request, jsonify
from flask_restful import Resource
import requests

from utils.settings import YOUTUBE_API_KEY


class Youtube(Resource):
    def post(self):
        try:
            query = request.get_json()
            url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'key': YOUTUBE_API_KEY if YOUTUBE_API_KEY else query['YOUTUBE_API_KEY'],
                'q': query['query'],
                'part': 'snippet',
                'maxResults': 15,
                'type': 'video'
            }
            r = requests.get(url, params=params)
            results = r.json()['items']
            data_videos = []
            for result in results:
                video = {
                    "image_url": result["snippet"]["thumbnails"]["high"]["url"],
                    "title": result["snippet"]["title"],
                    "description": str(result["snippet"]["description"])[:100]
                }
                data_videos.append(video)
            return jsonify({"data_videos": data_videos})
        except Exception as e:
            message = "You have an error, so we can not process your request, {}".format(
                e)
            return jsonify({'message': message})
