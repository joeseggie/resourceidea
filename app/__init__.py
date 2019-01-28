from flask_migrate import Migrate

from app.resourceidea import app, db
from app.models import (
    assignment_status,
    assignment,
    client_industry,
    client,
    company,
    currency,
    department,
    employee,
    invoice,
    job_comment,
    job_position,
    job_status,
    job_task,
    job,
    line_of_service,
    payment_method,
    receipt,
    resource,
    service_plan,
    subscription,
    user_account
)
from app.routes.api.index import index_blueprint
from app.routes.api.company import company_blueprint


migrate = Migrate(app, db)

app.register_blueprint(
    index_blueprint,
    url_prefix='/api/v1.0'
)

app.register_blueprint(
    company_blueprint,
    url_prefix='/api/v1.0/companies'
)
