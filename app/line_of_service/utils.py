"""Line of service utils."""
from uuid import UUID

from app.line_of_service.models import LineOfService
from app.line_of_service.repositories import LineOfServiceRepository


def create_line_of_service(**kwargs) -> LineOfService:
    """
    Create a new line of service.

    Returns:
        New line of service.
    """
    return LineOfServiceRepository.create(LineOfService(name=kwargs['name']))


def update_line_of_service(
        line_of_service_id: UUID, **kwargs) -> LineOfService:
    """
    Update line of service.

    Returns:
        Updated line of service.
    """
    update_fields = ('name',)
    return LineOfServiceRepository.update_by_id(
        model_id=line_of_service_id,
        fields_for_update=update_fields,
        **kwargs)


def get_line_of_service(line_of_service_id: UUID) -> LineOfService:
    """
    Get line of service by ID.

    Args:
        line_of_service_id (UUID): Line of service ID.

    Returns:
        Line of service.
    """
    return LineOfServiceRepository.get_one_by_id(model_id=line_of_service_id)
