from flask_restful import fields, marshal, reqparse, Resource

from ..models.assignment_status import AssignmentStatus
from database import db


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
        assignment_statuses = AssignmentStatus.query.all()
        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment_statuses,
        }

        return marshal(response, assignment_status_fields), 200

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'description',
            required=True,
            help='Description is required'
        )
        args = parser.parse_args()
        new_assignment_status = AssignmentStatus(description=args.description)
        db.session.add(new_assignment_status)
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 201,
            'data': new_assignment_status
        }
        return marshal(response, assignment_status_fields), 201


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
