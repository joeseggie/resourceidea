import enum


class OrganizationStatus(enum.Enum):
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'
