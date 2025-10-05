"""Controller for paint-related operations."""
from apps.core.models.paint import Paint
from apps.packpage.generic_controller import GenericController


class PaintController(GenericController):
    """Controller for paint-related operations."""

    def __init__(self) -> None:
        super().__init__(Paint)
