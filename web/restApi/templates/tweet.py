class Tweet:
    def __init__(self, text: str, predicted_label=None):
        self.text = text
        self.predicted_label = predicted_label
