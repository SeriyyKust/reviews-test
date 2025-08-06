from typing import Sequence
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from reviews.schemas import ReviewCreateSchema
from reviews.models import ReviewModel
from reviews.services.definition_sentiment import definition_sentiment_service


async def add_review_to_db(
        session: AsyncSession,
        new_review: ReviewCreateSchema
) -> ReviewModel:
    db_new_review = ReviewModel(
        text=new_review.text,
        # Задача является CPU-Bound и блокирует асинхронное выполнения
        # Так как размер отзыва ограничен (5000 символов) в данном случает блокировка будет не большой (её можно не учитывать)
        # При увеличении количества символов необходимо рассмотреть другой способ определения sentiment
        sentiment=definition_sentiment_service.execute(new_review.text)
    )
    session.add(db_new_review)
    await session.commit()
    await session.refresh(db_new_review)
    return db_new_review


async def get_reviews_from_db_by_sentiment(
        session: AsyncSession,
        sentiment: str
) -> Sequence[ReviewModel]:
    query = select(ReviewModel).where(ReviewModel.sentiment==sentiment)
    result: Result = await session.execute(query)
    return result.scalars().all()
