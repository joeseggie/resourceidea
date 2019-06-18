"""app.common.enums module"""
import enum


class OrganizationStatus(enum.Enum):
    """Organization status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'


class EngagementStatus(enum.Enum):
    """Engagement status enumeration."""
    NOT_STARTED = 'not started'
    RUNNING = 'running'
    IN_REVIEW = 'in review'
    REVIEWED = 'reviewed'
    CLOSED = 'closed'
