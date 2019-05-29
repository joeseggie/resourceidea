import ast

from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from app.auth.schemas import SignupInputSchema
from app.auth.schemas import SignupOutputSchema
from app.auth.utils import signup


auth_bp = Blueprint('auth', __name__)
auth_api = Api(auth_bp)


class Signup(Resource):
    def post(self):
        try:
            payload = request.json
            validated_input = SignupInputSchema(strict=True)\
                .load(payload).data
            new_organization = signup(**validated_input)
            status = 'OK'
            status_code = 201
        except IntegrityError as error:
            status_code = 400
            new_organization = None
            status, __ = error.orig.args

        output = SignupOutputSchema(strict=True)\
            .dump({
                'status': status,
                'data': new_organization
            }).data
        return output, status_code


auth_api.add_resource(Signup, '/signup')
