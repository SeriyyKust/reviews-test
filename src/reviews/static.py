from enum import Enum


class StatusSentiment(str, Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"
