from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.user.schemas import UserInputSchema
from app.user.schemas import UsersListFilterSchema
from app.user.schemas import UsersListSchema
from app.user.utils import get_all_users
from app.user.utils import create_user


user_bp = Blueprint('users', __name__)
user_api = Api(user_bp)
USER_ENDPOINT_PREFIX = '/users'


class UserAccountsListResource(Resource):
    def get(self):
        args = request.args
        validated_input = UsersListFilterSchema(strict=True)\
            .load(args).data
        users_list = get_all_users(**validated_input)
        output = UsersListSchema(strict=True).dump(
            {
                'status': 'OK',
                'code': 200,
                'data': users_list}).data
        return output, 200

    def post(self):
        payload = request.json
        validated_input = UserInputSchema(strict=True).load(payload).data
        new_user = create_user(**validated_input)
        output = {
            {
                'status': 'OK',
                'code': 201,
                'data': new_user
            }
        }
        return output


user_api.add_resource(UserAccountsListResource, USER_ENDPOINT_PREFIX)
