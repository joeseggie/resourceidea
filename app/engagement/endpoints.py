"""app.engagement.endpoints module"""
from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.engagement.schemas import EngagementSchema
from app.engagement.utils import create_engagement


engagement_bp = Blueprint('engagement', __name__)
engagement_api = Api(engagement_bp)
URL_PREFIX = '/engagements'


class EngagementsResource(Resource):
    """Engagements resource"""

    status_code = 200

    def post(self):
        """HTTP POST method handler."""
        payload = request.json
        valid_input = EngagementSchema(strict=True).load(payload).data
        new_engagement = create_engagement(**valid_input)
        output = EngagementSchema(strict=True).dump(new_engagement).data
        self.status_code = 201
        return output, self.status_code


engagement_api.add_resource(EngagementsResource, URL_PREFIX)
