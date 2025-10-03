"""Controller for paint-related operations."""
from app.models.paint import Paint
from app.utils.generic_controller import GenericController


class PaintController(GenericController):
    """Controller for paint-related operations."""

    def __init__(self) -> None:
        super().__init__(Paint)
