"""Client industry endpoints"""
import json

from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.client_industry.schemas import ClientIndustrySchema
from app.client_industry.utils import create_client_industry


client_industry_bp = Blueprint('client_industry', __name__)
client_industry_api = Api(client_industry_bp)
URL_PREFIX = '/clientindustries'


class ClientIndustriesResource(Resource):
    """ClientIndustries API resource."""

    status_code = 200

    def post(self):
        """HTTP POST method handler."""
        payload = request.json
        valid_input = ClientIndustrySchema(strict=True)\
            .load(payload).data
        try:
            new_client_industry = create_client_industry(**valid_input)
        except ValueError as error:
            output = json.dumps({'message': str(error)})
            self.status_code = 400
        else:
            output = ClientIndustrySchema(strict=True)\
                .dump(new_client_industry).data
            self.status_code = 201
        return output, self.status_code


client_industry_api.add_resource(ClientIndustriesResource, URL_PREFIX)
