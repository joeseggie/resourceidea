from flask_restful import fields, Resource, marshal_with


from ..models.service_plan import ServicePlan


data_fields = {}
data_fields['id'] = fields.Integer(attribute='id')
data_fields['name'] = fields.String(attribute='name')
data_fields['price'] = fields.Float(attribute='price')

service_plan_fields = {
    'status': fields.String,
    'code': fields.Integer,
    'message': fields.String
}

service_plan_fields['data'] = fields.Nested(data_fields)
service_plan_fields['details'] = {}


class ServicePlanResource(Resource):
    @marshal_with(service_plan_fields)
    def get(self):
        service_plans = ServicePlan.query.all()
        response = {
            'status': 'OK',
            'code': 200,
            'data': service_plans,
            'message': None,
            'details': None
        }
        return response, 200
