"""app.common.enums module"""
import enum

from app.common import constants


class OrganizationStatus(enum.Enum):
    """Organization status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'


class EngagementStatus(enum.Enum):
    """Engagement status enumeration."""
    NOT_STARTED = constants.NOT_STARTED
    RUNNING = constants.RUNNING
    IN_REVIEW = constants.IN_REVIEW
    REVIEWED = constants.REVIEWED
    CLOSED = constants.CLOSED


class JobStatus(enum.Enum):
    """Job status enumeration"""
    NOT_STARTED = constants.NOT_STARTED
    IN_PROGRESS = constants.IN_PROGRESS
    IN_REVIEW = constants.IN_REVIEW
    REVIEWED = constants.REVIEWED
    CLOSED = constants.CLOSED


class TaskStatus(enum.Enum):
    """Task status enumeration"""
    NOT_STARTED = constants.NOT_STARTED
    IN_PROGRESS = constants.IN_PROGRESS
    IN_REVIEW = constants.IN_REVIEW
    REVIEWED = constants.REVIEWED
    CLOSED = constants.CLOSED
