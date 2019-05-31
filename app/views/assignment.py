from datetime import datetime
from flask_restful import marshal, reqparse, Resource

from ..common.enveloper import AssignmentEnvelopeBuilder
from ..models.assignment import Assignment
from database import db


class AssignmentListResource(Resource):
    def get(self):
        assignments = Assignment.query.all()
        assignment_fields = AssignmentEnvelopeBuilder.ok_envelope()
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

        assignment_fields = AssignmentEnvelopeBuilder.ok_envelope()
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
            assignment_fields = AssignmentEnvelopeBuilder.ok_envelope()
            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            assignment_fields = AssignmentEnvelopeBuilder.error_envelope()
            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }
            response = {
                'status': 'ERROR',
                'code': status_code,
                'data': None,
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

            assignment_fields = AssignmentEnvelopeBuilder.ok_envelope()

            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            assignment_fields = AssignmentEnvelopeBuilder.error_envelope()
            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }
            response = {
                'status': 'ERROR',
                'code': status_code,
                'data': None,
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

            assignment_fields = AssignmentEnvelopeBuilder.ok_envelope()

            response = {
                'status': 'OK',
                'code': status_code,
                'data': assignment
            }
        else:
            status_code = 404
            assignment_fields = AssignmentEnvelopeBuilder.error_envelope()
            error = {
                'error_message': 'Resource Not Found',
                'detailed_error': 'Assignment with the Id supplied does not '
                                  'exist or is invalid.'
            }
            response = {
                'status': 'ERROR',
                'code': status_code,
                'data': None,
                'error': error
            }

        return marshal(response, assignment_fields), status_code
