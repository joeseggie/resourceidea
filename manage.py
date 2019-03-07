from app import app
from app.models.service_plan import ServicePlan
from database import db


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, ServicePlan=ServicePlan)
