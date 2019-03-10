from flask_restful import fields, marshal, reqparse, Resource

from database import db
from ..models.service_plan import ServicePlan


data_fields = {}
data_fields['id'] = fields.Integer(attribute='id')
data_fields['name'] = fields.String(attribute='name')
data_fields['price'] = fields.Float(attribute='price')

service_plan_fields = {
    'status': fields.String,
    'code': fields.Integer,
}

service_plan_fields['data'] = fields.Nested(data_fields)


class ServicePlanListResource(Resource):
    def get(self):
        service_plans = ServicePlan.query.all()
        response = {
            'status': 'OK',
            'code': 200,
            'data': service_plans,
        }
        return marshal(response, service_plan_fields), 200

    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'name',
            required=True,
            help='Service plan name is required'
        )
        parser.add_argument(
            'price',
            required=True,
            type=float,
            help='Service plan price is required or value supplied is invalid'
        )
        args = parser.parse_args()
        service_plan = ServicePlan(name=args.name, price=args.price)
        db.session.add(service_plan)
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 201,
            'data': service_plan
        }

        return marshal(response, service_plan_fields), 201


class ServicePlanResource(Resource):
    def put(self, id: int):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'name',
            required=True,
            help='Service plan name is required'
        )
        parser.add_argument(
            'price',
            required=True,
            type=float,
            help='Service plan price is required or value supplied is invalid'
        )
        args = parser.parse_args()

        service_plan = ServicePlan.query.get(id)
        service_plan.name = args.name
        service_plan.price = args.price
        db.session.commit()

        response = {
            'status': 'OK',
            'code': 200,
            'data': service_plan
        }
        return marshal(response, service_plan_fields), 200

    def get(self, id: int):
        service_plan = ServicePlan.query.get(id)
        response = {
            'status': 'OK',
            'code': 200,
            'data': service_plan
        }
        return marshal(response, service_plan_fields), 200
