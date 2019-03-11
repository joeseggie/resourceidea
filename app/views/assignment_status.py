from flask_restful import fields, marshal, Resource

from ..models.assignment_status import AssignmentStatus


assignment_status_fields = {
    'id': fields.Integer,
    'description': fields.String
}


class AssignmentStatusListResource(Resource):
    def get(self):
        assignment_statuses = AssignmentStatus.query.all()
        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment_statuses,
        }

        return marshal(response, assignment_status_fields), 200
