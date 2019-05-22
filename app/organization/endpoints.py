from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.organization.schemas import CompanyCreatedSchema
from app.organization.schemas import CompanyInputSchema
from app.organization.schemas import CompanyListFilterSchema
from app.organization.schemas import CompanyListSchema
from app.organization.utils import create_organization
from app.organization.utils import get_organizations


company_bp = Blueprint('organization', __name__)
company_api = Api(company_bp)
ENDPOINT_PREFIX = '/companies'


class CompanyListResource(Resource):
    def get(self):
        args = request.args
        validated_input = CompanyListFilterSchema(strict=True)\
            .load(args).data
        companies_list = get_organizations(**validated_input)
        output = CompanyListSchema(strict=True).dump(
            {
                'status': 'OK',
                'code': 200,
                'data': companies_list
            }
        ).data
        return output, 200

    def post(self):
        payload = request.json
        validated_input = CompanyInputSchema(strict=True)\
            .load(payload).data
        new_company = create_organization(**validated_input)
        output = CompanyCreatedSchema(strict=True).dump({
            'status': 'OK',
            'code': 201,
            'data': new_company
        }).data
        return output, 201


company_api.add_resource(CompanyListResource, f'{ENDPOINT_PREFIX}')
