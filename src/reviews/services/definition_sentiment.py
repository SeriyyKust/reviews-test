import re
from reviews.static import StatusSentiment, GOOD_WORDS, BAD_WORDS


class DefinitionSentimentService:

    def __init__(self, good_words: set[str], bad_words: set[str]) -> None:
        self._good_words: set[str] = good_words
        self._bad_words: set[str] = bad_words

    def execute(self, text: str) -> StatusSentiment:
        text = text.lower()
        words = re.findall(r"\w+", text)
        good_count: int = 0
        bad_count: int = 0
        for word in words:
            if word in self._good_words:
                good_count += 1
            elif word in self._bad_words:
                bad_count += 1
        if good_count > bad_count:
            return StatusSentiment.positive
        elif bad_count > good_count:
            return StatusSentiment.negative
        else:
            return StatusSentiment.neutral


# В дальнейшем мы можем вынести слова в отдельный файл и подгружать их оттуда
# На данный момент слова определены статично в коде
definition_sentiment_service = DefinitionSentimentService(
    good_words=GOOD_WORDS,
    bad_words=BAD_WORDS
)