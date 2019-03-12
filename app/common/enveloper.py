from flask_restful import fields


class AssignmentEnvelopeBuilder:
    '''
    Builds the envelope for OK API responses.
    '''

    @staticmethod
    def base_envelope():
        '''
        Constructor
        '''
        assignment_envelope = {
            'status': fields.String,
            'code': fields.Integer,
        }
        return assignment_envelope

    @classmethod
    def ok_envelope(cls):
        '''
        Envelope for OK response.
        '''
        data_fields = {}
        data_fields['id'] = fields.Integer(attribute='id')
        data_fields['starts'] = fields.String(attribute='starts')
        data_fields['ends'] = fields.String(attribute='ends')
        assignment_envelope = cls.base_envelope()
        assignment_envelope['data'] = fields.Nested(data_fields)

        return assignment_envelope

    @classmethod
    def error_envelope(cls):
        '''
        Envelope for error response.
        '''
        error_fields = {}
        error_fields['message'] = fields.String(attribute='error_message')
        error_fields['details'] = fields.String(attribute='detailed_error')
        assignment_envelope = cls.base_envelope()
        assignment_envelope['error'] = fields.Nested(error_fields)

        return assignment_envelope
