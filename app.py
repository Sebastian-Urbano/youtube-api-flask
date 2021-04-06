from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# resources import
from resources.youtube import Youtube

application = Flask(__name__)
api = Api(application)
cors = CORS(application, resources={r"/*": {"origins": "*"}})


@application.route('/')
def index():
    return ({'message': 'welcome to the youtube api'})


api.add_resource(Youtube, '/youtube-search')

if __name__ == '__main__':
    # application.run(debug=True)
    application.run(host='0.0.0.0', port=5000)
