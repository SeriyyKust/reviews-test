from typing import Annotated

from database import get_database_session
from fastapi import APIRouter, Depends, Query
from reviews.schemas import ReviewBaseSchema, ReviewCreateSchema, StatusSentiment
from reviews.services.crud import add_review_to_db, get_reviews_from_db_by_sentiment
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post(
    path="/", summary="Добавление нового отзыва", response_model=ReviewBaseSchema
)
async def api_create_review(
    new_review: ReviewCreateSchema, session: AsyncSession = Depends(get_database_session)
):
    return await add_review_to_db(session=session, new_review=new_review)


@router.get(
    path="/",
    summary="Получение отзывов определённого статуса",
    response_model=list[ReviewBaseSchema],
)
async def api_get_reviews_by_sentiment(
    sentiment: Annotated[StatusSentiment, Query(title="Статус отзыва")],
    session: AsyncSession = Depends(get_database_session),
):
    return await get_reviews_from_db_by_sentiment(session=session, sentiment=sentiment)
