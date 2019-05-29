from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.organization.schemas import OrganizationCreatedSchema
from app.organization.schemas import OrganizationInputSchema
from app.organization.schemas import OrganizationListFilterSchema
from app.organization.schemas import OrganizationListSchema
from app.organization.utils import create_organization
from app.organization.utils import get_organizations


organization_bp = Blueprint('organization', __name__)
organization_api = Api(organization_bp)
URL_PREFIX = '/organizations'


class OrganizationListResource(Resource):
    def get(self):
        args = request.args
        validated_input = OrganizationListFilterSchema(strict=True)\
            .load(args).data
        companies_list = get_organizations(**validated_input)
        output = OrganizationListSchema(strict=True).dump(
            {
                'status': 'OK',
                'code': 200,
                'data': companies_list
            }
        ).data
        return output, 200

    def post(self):
        payload = request.json
        validated_input = OrganizationInputSchema(strict=True)\
            .load(payload).data
        new_company = create_organization(**validated_input)
        output = OrganizationCreatedSchema(strict=True).dump({
            'status': 'OK',
            'code': 201,
            'data': new_company
        }).data
        return output, 201


organization_api.add_resource(OrganizationListResource, URL_PREFIX)
