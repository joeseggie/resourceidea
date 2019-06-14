"""app.client.endpoints module"""
from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.client.schemas import ClientSchema
from app.client.utils import create_client

client_bp = Blueprint('client', __name__)
client_api = Api(client_bp)
URL_PREFIX = '/clients'


class ClientsResource(Resource):
    """Clients resource"""
    status_code = 200

    def post(self):
        """HTTP POST method handler."""
        payload = request.json
        valid_input = ClientSchema(strict=True).load(payload).data
        new_client = create_client(**valid_input)
        output = ClientSchema(strict=True).dump(new_client).data
        self.status_code = 201
        return output, self.status_code


client_api.add_resource(ClientsResource)
