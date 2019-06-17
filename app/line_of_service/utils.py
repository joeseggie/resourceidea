"""Line of service utils."""
from app.line_of_service.models import LineOfService
from app.line_of_service.repositories import LineOfServiceRepository


def create_line_of_service(**kwargs) -> LineOfService:
    """
    Create a new line of service.

    Returns:
        New line of service.
    """
    return LineOfServiceRepository.create(LineOfService(name=kwargs['name']))
