from src.reviews.static import StatusSentiment

from .fixture import get_definition_sentiment_service


def test_positive_sentiment(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это супер тест"
    assert definition_sentiment_service.execute(text) == StatusSentiment.positive


def test_positive_sentiment_hard(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это супер тест с великолепно сформированной целью но ужасно простой"
    assert definition_sentiment_service.execute(text) == StatusSentiment.positive


def test_negative_sentiment(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это ужасно составленный тест"
    assert definition_sentiment_service.execute(text) == StatusSentiment.negative


def test_negative_sentiment_hard(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это супер тест с великолепно сформированной целью но ужасно простой и плохо написанный просто кошмар"
    assert definition_sentiment_service.execute(text) == StatusSentiment.negative


def test_neutral_sentiment(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это тест"
    assert definition_sentiment_service.execute(text) == StatusSentiment.neutral


def test_neutral_sentiment_hard(get_definition_sentiment_service):
    definition_sentiment_service = get_definition_sentiment_service
    text = "Это супер тест с великолепно сформированной целью но ужасно простой и плохо написанный"
    assert definition_sentiment_service.execute(text) == StatusSentiment.neutral
