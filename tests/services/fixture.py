import pytest
from src.reviews.services.definition_sentiment import DefinitionSentimentService


@pytest.fixture()
def get_definition_sentiment_service() -> DefinitionSentimentService:
    """
    :return: Возвращает экземпляр DefinitionSentimentService определённый простыми словами
    """
    good_words = {
        "отлично",
        "хорошо",
        "замечательно",
        "супер",
        "прекрасно",
        "потрясающе",
        "великолепно",
    }
    bad_words = {
        "плохо",
        "ужасно",
        "отвратительно",
        "кошмар",
        "ненавижу",
        "тупо",
        "глупо",
    }
    definition_sentiment_service = DefinitionSentimentService(
        good_words=good_words, bad_words=bad_words
    )
    return definition_sentiment_service
