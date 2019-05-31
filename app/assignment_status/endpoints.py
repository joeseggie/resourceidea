from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import fields
from flask_restful import marshal
from flask_restful import reqparse
from flask_restful import Resource

from database import db
from .models import AssignmentStatus
from .repository import AssignmentStatusRepository
from .schemas import AssignmentStatusListOutputSchema
from .schemas import NewAssignmentStatusInputSchema
from .schemas import NewAssignmentStatusOutputSchema


assignment_status_bp = Blueprint('assignmentstatus', __name__)
assignment_status_api = Api(assignment_status_bp)
ENDPOINT_PREFIX = '/assignmentstatus'


data_fields = {}
data_fields['id'] = fields.Integer(attribute='id')
data_fields['description'] = fields.String(attribute='description')

assignment_status_fields = {
    'status': fields.String,
    'code': fields.Integer
}
assignment_status_fields['data'] = fields.Nested(data_fields)


class AssignmentStatusListResource(Resource):
    def get(self):
        assignment_statuses = AssignmentStatusRepository.list_all()
        output = AssignmentStatusListOutputSchema(strict=True).dump(assignment_statuses).data
        return output, 200

    def post(self):
        args = request.json
        validated_input = NewAssignmentStatusInputSchema(strict=True).load(args).data
        assignment_status = AssignmentStatusRepository.save(description=validated_input)
        output = NewAssignmentStatusOutputSchema(strict=True).dump(assignment_status).data
        return output, 201


class AssignmentStatusResource(Resource):
    def get(self, id: int):
        assignment_status = AssignmentStatus.query.get(id)
        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment_status
        }
        return marshal(response, assignment_status_fields), 200

    def put(self, id: int):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'description',
            required=True,
            help='Description is required'
        )
        args = parser.parse_args()
        assignment_status = AssignmentStatus.query.get(id)
        assignment_status.description = args.description
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment_status
        }
        return marshal(response, assignment_status_fields)


assignment_status_api.add_resource(AssignmentStatusListResource, f'{ENDPOINT_PREFIX}')
assignment_status_api.add_resource(AssignmentStatusResource, f'{ENDPOINT_PREFIX}/<int:id>')
