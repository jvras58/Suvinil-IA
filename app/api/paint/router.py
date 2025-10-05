"""Paint-related API routes and operations."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi import status as HTTP_STATUS
from sqlalchemy.orm import Session

from app.api.authentication.controller import get_current_user
from app.api.authorization.controller import validate_transaction_access
from app.api.paint.controller import PaintController
from app.api.paint.schema import PaintList, PaintPublic, PaintSchema
from app.api.transaction.enum_operation_code import EnumOperationCode as op
from app.database.session import get_session
from app.models.paint import Paint
from app.models.user import User
from app.utils.base_schemas import SimpleMessageSchema
from app.utils.client_ip import get_client_ip
from app.utils.exceptions import (
    IntegrityValidationException,
    ObjectNotFoundException,
)

router = APIRouter()
paint_controller = PaintController()

DbSession = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/', status_code=201, response_model=PaintPublic)
async def create_new_paint(
    paint: PaintSchema,
    request: Request,
    session: DbSession,
    current_user: CurrentUser,
):
    """Create a new paint."""
    validate_transaction_access(session, current_user, op.OP_1060001.value)

    new_paint: Paint = Paint(**paint.model_dump())
    new_paint.audit_user_ip = get_client_ip(request)
    new_paint.audit_user_login = current_user.username

    try:
        return paint_controller.save(session, new_paint)
    except IntegrityValidationException as ex:
        raise HTTPException(
            status_code=HTTP_STATUS.HTTP_400_BAD_REQUEST,
            detail='Object PAINT was not accepted',
        ) from ex


@router.get(
    '/{paint_id}',
    status_code=HTTP_STATUS.HTTP_200_OK,
    response_model=PaintPublic,
)
def get_paint_by_id(
    paint_id: int, db_session: DbSession, current_user: CurrentUser
):
    """Get paint by ID."""
    validate_transaction_access(db_session, current_user, op.OP_1060005.value)

    try:
        return paint_controller.get(db_session, paint_id)
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex


@router.get('/', response_model=PaintList)
def read_paints(
    db_session: DbSession,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
):
    """Retrieve all paints with pagination."""
    validate_transaction_access(db_session, current_user, op.OP_1060003.value)
    paints: list[Paint] = paint_controller.get_all(db_session, skip, limit)
    return {'paints': paints}


@router.put('/{paint_id}', response_model=PaintPublic)
def update_existing_paint(
    paint_id: int,
    paint: PaintSchema,
    request: Request,
    db_session: DbSession,
    current_user: CurrentUser,
):
    """Update an existing paint."""
    validate_transaction_access(db_session, current_user, op.OP_1060002.value)

    try:
        new_paint: Paint = Paint(**paint.model_dump())
        new_paint.id = paint_id

        new_paint.audit_user_ip = get_client_ip(request)
        new_paint.audit_user_login = current_user.username

        return paint_controller.update(db_session, new_paint)
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex


@router.delete('/{paint_id}', response_model=SimpleMessageSchema)
def delete_existing_paint(
    paint_id: int,
    db_session: DbSession,
    current_user: CurrentUser,
):
    """Delete a paint by ID."""
    validate_transaction_access(db_session, current_user, op.OP_1060004.value)

    try:
        paint_controller.delete(db_session, paint_id)
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex

    return {'detail': 'Paint deleted'}
