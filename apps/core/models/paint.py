"""Model for Paint (Tinta)."""
from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.core.api.paint.paint_enums import (
    Environment,
    FinishType,
    PaintLine,
    SurfaceType,
)
from apps.packpage.base_model import AbstractBaseModel

if TYPE_CHECKING:
    from apps.core.models.user import User


class Paint(AbstractBaseModel):
    """
    Represents the Paint (Tinta) table in the system.
    """

    __tablename__ = 'paint'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    name: Mapped[str] = mapped_column(name='str_name')
    color: Mapped[str] = mapped_column(name='str_color')
    surface_type: Mapped[SurfaceType] = mapped_column(
        Enum(SurfaceType), name='enum_surface_type'
    )
    environment: Mapped[Environment] = mapped_column(
        Enum(Environment), name='enum_environment'
    )
    finish_type: Mapped[FinishType] = mapped_column(
        Enum(FinishType), name='enum_finish_type'
    )
    features: Mapped[str | None] = mapped_column(
        String(500), name='str_features', nullable=True
    )
    paint_line: Mapped[PaintLine] = mapped_column(
        Enum(PaintLine), name='enum_paint_line'
    )
    created_by_user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), name='created_by_user_id', nullable=False
    )

    created_by_user: Mapped["User"] = relationship(
        back_populates="paints", lazy="subquery"
    )

    __table_args__ = (
        Index('idx_paint_name', name),
        Index('idx_paint_color', color),
        Index('idx_paint_surface_type', surface_type),
        Index('idx_paint_environment', environment),
        Index('idx_paint_line', paint_line),
    )
