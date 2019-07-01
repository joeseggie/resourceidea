"""app.task.endpoints module"""
from uuid import UUID

from flask import Blueprint
from flask import request
from flask_restful import Api
from flask_restful import Resource

from app.task.schemas import TaskSchema
from app.task.utils import create_task
from app.task.utils import get_task
from app.task.utils import list_tasks
from app.task.utils import update_task


task_bp = Blueprint('task', __name__)
task_api = Api(task_bp)
URL_PREFIX = '/tasks'


class TasksResource(Resource):
    """Tasks resource."""

    status_code = 200

    def post(self):
        """HTTP POST method handler"""
        user_input = request.json
        valid_input = TaskSchema(strict=True).load(user_input).data
        new_task = create_task(**valid_input)
        output = TaskSchema(strict=True).dump(new_task).data
        self.status_code = 201
        return output, self.status_code

    def get(self):
        """HTTP POST method handler"""
        tasks = list_tasks()
        output = TaskSchema(strict=True, Many=True).dump(tasks).data
        return output, self.status_code


class TaskResource(Resource):
    """Task resource"""

    status_code = 200

    def get(self, task_id: UUID):
        """HTTP GET method handler."""
        task_query = get_task(task_id)
        output = TaskSchema(strict=True).dump(task_query).data
        return output, self.status_code

    def put(self, task_id: UUID):
        """HTTP PUT method handler."""
        user_input = request.json
        valid_input = TaskSchema(strict=True).load(user_input).data
        updated_task = update_task(task_id, **valid_input)
        output = TaskSchema(strict=True).dump(updated_task).data
        return output, self.status_code


task_api.add_resource(TasksResource, URL_PREFIX)
task_api.add_resource(TaskResource, f'{URL_PREFIX}/<uuid:task_id>')
