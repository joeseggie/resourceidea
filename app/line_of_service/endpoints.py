"""Line of service endpoints."""
from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.line_of_service.schemas import LineOfServiceSchema
from app.line_of_service.utils import create_line_of_service


line_of_service_bp = Blueprint('line_of_service', __name__)
line_of_service_api = Api(line_of_service_bp)
URL_PREFIX = '/linesofservice'


class LinesOfServiceResource(Resource):
    """Lines of service resource."""

    status_code = 200

    def post(self):
        """HTTP POST Method handler."""
        payload = request.json
        valid_input = LineOfServiceSchema(strict=True).load(payload).data
        new_los = create_line_of_service(**valid_input)
        output = LineOfServiceSchema(strict=True).dump(new_los).data
        self.status_code = 201
        return output, self.status_code


line_of_service_api.add_resource(LinesOfServiceResource, URL_PREFIX)
