"""app.job.endpoints module"""
from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource

from app.job.schemas import JobSchema
from app.job.utils import list_jobs


job_bp = Blueprint('job', __name__)
job_api = Api(job_bp)
URL_PREFIX = '/jobs'


class JobsResource(Resource):
    """Job resource"""

    status_code = 200

    def get(self):
        """HTTP GET method handler"""
        jobs_list = list_jobs()
        output = JobSchema(strict=True, many=True).dump(jobs_list).data
        return output, self.status_code
