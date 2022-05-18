class Tweet:
    def __init__(self, text: str, predicted_label=None, processed_view: list = None):
        self.text = text
        self.predicted_label = predicted_label
        self.processed_view = processed_view