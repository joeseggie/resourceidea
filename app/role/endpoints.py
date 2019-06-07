from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource
from uuid import UUID

from app.role.schemas import RoleSchema
from app.role.utils import get_role
from app.role.utils import list_roles


role_bp = Blueprint('role', __name__)
role_api = Api(role_bp)
ROLE_PREFIX = '/roles'


class RolesListResource(Resource):
    def get(self):
        args = request.args
        validated_input = RoleSchema(strict=True).load(args).data
        roles_list = list_roles(validated_input)
        output = RoleSchema(strict=True, many=True).dump(roles_list).data
        return output, 200


class RoleResource(Resource):
    def get(self, role_id: UUID):
        role = get_role(role_id)
        output = RoleSchema(strict=True).dump(role).data
        return output, 200


role_api.add_resource(RolesListResource, ROLE_PREFIX)
role_api.add_resource(RoleResource, f'{ROLE_PREFIX}/<string:role_id>')
