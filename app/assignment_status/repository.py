from .models import AssignmentStatus
from database import db


class AssignmentStatusRepository():

    @staticmethod
    def save(**kwargs):
        '''
        Add new assignment status.
        '''
        description = kwargs.get('description', '')
        status_exists = AssignmentStatus.query.filter(AssignmentStatus.description == description).all()
        if not status_exists:
            new_assignment_status = AssignmentStatus(description=description)
            db.session.add(new_assignment_status)
            db.session.commit()
            return {
                'status': 'OK',
                'code': 201,
                'data': new_assignment_status
            }
        else:
            raise ValueError('Status already exists.')

    def update(self, status_update: dict):
        '''
        update existing assignment status.
        '''
        status_exists = AssignmentStatus.query.filter_by(description=self.description).items
        if status_exists and status_exists.id == status_update['id']:
            assignment_status = AssignmentStatus.query.get(status_update['id'])
            assignment_status.description = status_update['description']
            db.session.commit()
        elif not status_exists:
            raise ValueError('Assignment status does not exists.')
        elif status_exists and status_exists.id != status_update['id']:
            raise ValueError('Assignment with same description already exists')

    def get(self, id: int):
        '''
        Get the assignment status given the Id.

        Arguments:
        id {int}
            Assignment status Id.

        Returns:
        AssignmentStatus
            Assignment status details.
        '''
        assignment_status = AssignmentStatus.query.get(id).first()
        if assignment_status:
            return assignment_status
        else:
            raise ValueError('Assignment status with the Id does not exist.')

    @staticmethod
    def list_all():
        assignment_statuses = AssignmentStatus.query.all()
        return {
            'status': 'OK',
            'code': 200,
            'data': assignment_statuses
        }
