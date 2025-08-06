from pydantic import BaseModel, ConfigDict, Field
from reviews.static import MAX_LENGTH_REVIEW_TEXT, StatusSentiment


class ReviewCreateSchema(BaseModel):
    text: str = Field(
        title="Текст отзыва", min_length=1, max_length=MAX_LENGTH_REVIEW_TEXT
    )


class ReviewBaseSchema(ReviewCreateSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(title="Идентификатор отзыва", ge=0)
    sentiment: StatusSentiment
    created_at: str
