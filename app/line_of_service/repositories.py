"""app.line_of_service.repositories module"""
from app.common.base_repository import BaseRepository
from app.line_of_service.models import LineOfService


class LineOfServiceRepository(BaseRepository):
    """Line of service repository."""
    model_class = LineOfService
