from datetime import datetime
from flask_restful import fields, marshal, reqparse, Resource

from database import db
from ..models.assignment import Assignment


assignment_fields = {
    'status': fields.String,
    'code': fields.Integer,
}


class AssignmentListResource(Resource):
    def get(self):
        assignments = Assignment.query.all()

        data_fields = {}
        data_fields['id'] = fields.Integer(attribute='id')
        data_fields['starts'] = fields.String(attribute='starts')
        data_fields['ends'] = fields.String(attribute='ends')
        assignment_fields['data'] = fields.Nested(data_fields)

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

        data_fields = {}
        data_fields['id'] = fields.Integer(attribute='id')
        data_fields['starts'] = fields.String(attribute='starts')
        data_fields['ends'] = fields.String(attribute='ends')
        assignment_fields['data'] = fields.Nested(data_fields)

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
        status_code = 200
        if assignment:

            data_fields = {}
            data_fields['id'] = fields.Integer(attribute='id')
            data_fields['starts'] = fields.String(attribute='starts')
            data_fields['ends'] = fields.String(attribute='ends')
            assignment_fields['data'] = fields.Nested(data_fields)

            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            error_fields = {}
            error_fields['message'] = fields.String(attribute='error_message')
            error_fields['details'] = fields.String(attribute='detailed_error')

            assignment_fields['error'] = fields.Nested(error_fields)

            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }

            response = {
                'status': 'ERROR',
                'code': status_code,
                'error': error
            }
        return marshal(response, assignment_fields), status_code

    def put(self, id: int):
        assignment = Assignment.query.get(id)
        status_code = 200
        if assignment:
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
            assignment.starts = args.starts
            assignment.ends = args.ends
            db.session.commit()

            data_fields = {}
            data_fields['id'] = fields.Integer(attribute='id')
            data_fields['starts'] = fields.String(attribute='starts')
            data_fields['ends'] = fields.String(attribute='ends')
            assignment_fields['data'] = fields.Nested(data_fields)

            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            error_fields = {}
            error_fields['message'] = fields.String(attribute='error_message')
            error_fields['details'] = fields.String(attribute='detailed_error')

            assignment_fields['error'] = fields.Nested(error_fields)

            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }

            response = {
                'status': 'ERROR',
                'code': status_code,
                'error': error
            }

        return marshal(response, assignment_fields), status_code

    def patch(self, id: int):
        status_code = 200
        assignment = Assignment.query.get(id)
        if assignment:
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
            if 'starts' in args and args.starts:
                assignment.starts = args.starts
            if 'ends' in args and args.ends:
                assignment.ends = args.ends
            db.session.commit()

            data_fields = {}
            data_fields['id'] = fields.Integer(attribute='id')
            data_fields['starts'] = fields.String(attribute='starts')
            data_fields['ends'] = fields.String(attribute='ends')
            assignment_fields['data'] = fields.Nested(data_fields)

            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            error_fields = {}
            error_fields['message'] = fields.String(attribute='error_message')
            error_fields['details'] = fields.String(attribute='detailed_error')

            assignment_fields['error'] = fields.Nested(error_fields)

            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }

            response = {
                'status': 'ERROR',
                'code': status_code,
                'error': error
            }

        return marshal(response, assignment_fields), status_code
