import logging
import os
import time

# import sentry_sdk
# from ddtrace import tracer
from flask import Flask
from flask import request, g
from flask_cors import CORS
from flask_restful import Api

from api_doc.apidoc import initialize_api_doc
# from common.data_dog import data_dog_body
from config.routes import api_v1_routes
from database.db import initialize_db

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)
logging.getLogger('flask_cors').level = logging.DEBUG
# initialize db
initialize_db(app)

# initialize routes
api_v1_routes(api, "/api/user/v1")

# initialize api doc
initialize_api_doc(app)

# initialize content length
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

app.config['MEDIA_ROOT'] = 'media/default/'

# DATA DOG

api_mode = os.environ.get("MODE", "LOCAL")


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
