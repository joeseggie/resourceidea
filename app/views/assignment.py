from datetime import datetime
from flask_restful import fields, marshal, reqparse, Resource

from database import db
from ..models.assignment import Assignment


assignment_fields = {
    'id': fields.Integer,
    'starts': fields.DateTime,
    'ends': fields.DateTime
}


class AssignmentListResource(Resource):
    def get(self):
        assignments = Assignment.query.all()
        response = {
            'status': 'OK',
            'code': 200,
            'data': assignments
        }
        return marshal(response, assignment_fields), 200

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'starts',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
            help='Assignment start date and time required'
        )
        parser.add_argument(
            'ends',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'),
            help='Assignment end date and time required'
        )
        args = parser.parse_args()
        assignment = Assignment(starts=args.starts, price=args.ends)
        db.session.add(assignment)
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 201,
            'data': assignment
        }
        return marshal(response, assignment_fields), 201
