"""app.engagement.endpoints module"""
from uuid import UUID

from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.engagement.schemas import EngagementSchema
from app.engagement.utils import create_engagement
from app.engagement.utils import update_engagement


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


class EngagementResource(Resource):
    """Engagement Resource"""

    status_code = 200

    def put(self, resource_id: str):
        """
        HTTP PUT method handler.

        Args:
            resource_id (str): Resource ID.
        """
        payload = request.json
        valid_input = EngagementSchema(strict=True).load(payload).data
        engagement_update = update_engagement(
            engagement_id=UUID(resource_id),
            **valid_input)
        output = EngagementSchema(strict=True).dump(engagement_update).data
        return output, self.status_code


engagement_api.add_resource(EngagementsResource, URL_PREFIX)
engagement_api.add_resource(
    EngagementResource,
    f'{URL_PREFIX}/<string:resource_id>')
