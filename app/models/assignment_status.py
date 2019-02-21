"""Assignment status model
"""
from database import db


class AssignmentStatus(db.Model):
    """Assignment status model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'assignment_status'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))

    def __repr__(self):
        return '<Assignment status %s>' % self.description

    def save(self):
        '''
        Add new assignment status.
        '''
        status_exists = AssignmentStatus.query.filter_by(
            description=self.description
        ).items
        if not status_exists:
            new_status = AssignmentStatus(description=self.description)
            db.session.add(new_status)
            db.session.commit()
        else:
            raise ValueError('Status already exists.')

    def update(self, status_update: dict):
        '''
        update existing assignment status.
        '''
        status_exists = AssignmentStatus.query.filter_by(
            description=self.description
        ).items
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
