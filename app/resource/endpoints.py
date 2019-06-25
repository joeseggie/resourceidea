"""app.resource.endpoints module"""
from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.resource.schemas import ResourceSchema
from app.resource.utils import create_resource


resource_bp = Blueprint('resources', __name__)
resource_api = Api(resource_bp)
URL_PREFIX = '/resources'


class ChargingEmployeeResource(Resource):
    """Resource for charging employees referred to as resources"""

    status_code = 200

    def post(self):
        """HTTP POST method handler"""
        payload = request.json
        valid_input = ResourceSchema(strict=True).load(payload).data
        new_resource = create_resource(**valid_input)
        output = ResourceSchema(strict=True).dump(new_resource).data
        self.status_code = 201
        return output, self.status_code
