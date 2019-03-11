from datetime import datetime
from flask_restful import fields, marshal, reqparse, Resource

from database import db
from ..models.assignment import Assignment


data_fields = {}
data_fields['id'] = fields.Integer(attribute='id')
data_fields['starts'] = fields.String(attribute='starts')
data_fields['ends'] = fields.String(attribute='ends')

assignment_fields = {
    'status': fields.String,
    'code': fields.Integer,
}
assignment_fields['data'] = fields.Nested(data_fields)


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
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment start date and time required'
        )
        parser.add_argument(
            'ends',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment end date and time required'
        )
        args = parser.parse_args()
        assignment = Assignment(starts=args.starts, ends=args.ends)
        db.session.add(assignment)
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 201,
            'data': assignment
        }
        return marshal(response, assignment_fields), 201


class AssignmentResource(Resource):
    '''
    Assignment resource.
    '''

    def get(self, id: int):
        assignment = Assignment.query.get(id)
        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment
        }
        return marshal(response, assignment_fields)

    def put(self, id: int):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'starts',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment start date and time required'
        )
        parser.add_argument(
            'ends',
            required=True,
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment end date and time required'
        )
        args = parser.parse_args()
        assignment = Assignment.query.get(id)
        assignment.starts = args.starts
        assignment.ends = args.ends
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment
        }
        return marshal(response, assignment_fields), 200

    def patch(self, id: int):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'starts',
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment start date and time required'
        )
        parser.add_argument(
            'ends',
            type=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'),
            help='Assignment end date and time required'
        )
        args = parser.parse_args()
        print(args)
        assignment = Assignment.query.get(id)
        if 'starts' in args and args.starts:
            assignment.starts = args.starts
        if 'ends' in args and args.ends:
            assignment.ends = args.ends
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 200,
            'data': assignment
        }
        return marshal(response, assignment_fields), 200
