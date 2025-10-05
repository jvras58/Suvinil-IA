"""Schemas for Paint model."""

from pydantic import BaseModel, ConfigDict

from apps.core.api.paint.paint_enums import (
    Environment,
    FinishType,
    PaintLine,
    SurfaceType,
)


class PaintSchema(BaseModel):
    """Schema for creating/updating paint."""

    name: str
    color: str
    surface_type: SurfaceType
    environment: Environment
    finish_type: FinishType
    features: str | None = None
    paint_line: PaintLine
    created_by_user_id: int


class PaintPublic(BaseModel):
    """Schema for public paint representation."""

    id: int
    name: str
    color: str
    surface_type: SurfaceType
    environment: Environment
    finish_type: FinishType
    features: str | None
    paint_line: PaintLine
    created_by_user_id: int
    model_config = ConfigDict(from_attributes=True)


class PaintList(BaseModel):
    """Schema for listing paints."""

    paints: list[PaintPublic]
