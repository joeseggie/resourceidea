from flask import Blueprint, jsonify

from app.queryables.company_queryable import CompanyQueryable


company_blueprint = Blueprint('company_blueprint', __name__)


@company_blueprint.route('/')
def list_companies():
    company_queryable = CompanyQueryable()
    companies_list = company_queryable.to_list()
    return jsonify(
        {
            'status': 200,
            'data': companies_list
        }
    )
