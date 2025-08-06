from datetime import datetime

from database import Base
from reviews.static import MAX_LENGTH_REVIEW_TEXT, StatusSentiment
from sqlalchemy import CheckConstraint, Enum, String
from sqlalchemy.orm import Mapped, mapped_column


class ReviewModel(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(MAX_LENGTH_REVIEW_TEXT), nullable=False)
    sentiment: Mapped[StatusSentiment] = mapped_column(
        Enum(StatusSentiment, name="sentiment_enum"),
        nullable=False,
        # Так как в дальнейшем поиск происходит по данному атрибуту
        # Решено его индексировать
        index=True,
    )
    created_at: Mapped[str] = mapped_column(
        String, default=lambda: datetime.utcnow().isoformat()
    )

    # Ограничение на пустую строку
    __table_args__ = (CheckConstraint("length(text) > 0", name="check_text_non_empty"),)
