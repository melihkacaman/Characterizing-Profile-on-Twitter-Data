import enum


@enum.unique
class TweetLabel(enum.IntEnum):
    POLITICS = 1
    FOOD = 2
    SPORT = 3
    TECHNOLOGY = 4


class Tweet:
    def __init__(self, text: str, predicted_label: TweetLabel = None, processed_view: list = None):
        self.text = text
        self.predicted_label = predicted_label
        self.processed_view = processed_view
