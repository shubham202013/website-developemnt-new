from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

def initialize_api_doc(app):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='PMS',
            version='v2',
            openapi_version="2.0",
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
    })
    docs = FlaskApiSpec(app)

   

