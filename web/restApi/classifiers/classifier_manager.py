import pickle
from utils import process_tweet

class ClassifierManager:
    def __init__(self, tweet_list: list):
        self.raw_tweets = tweet_list
        self.predicted_tweets = []
        self._politics_classifier = None
        self._food_classifier = None
        self._sport_classifier = None
        self._technology_classifier = None

        self._initialize_classifiers()
        self._predict_tweets()

    def _initialize_classifiers(self):
        # 1. Politics classifier : linear SVM
        with open('resources/politics_linearSVM2', 'rb') as f:
            self._politics_classifier = pickle.load(f)

        # 2. Food Classifier : Naive Bayes
        with open('resources/food_naivebayes.', 'rb') as f:
            self._food_classifier = pickle.load(f)

        # 3. Sport Classifier : Naive Bayes
        with open('resources/sport_naivebayes.', 'rb') as f:
            self._sport_classifier = pickle.load(f)

        # 4. Technology Classifier : Naive Bayes
        with open('resources/technology_naivebayes_', 'rb') as f:
            self._politics_classifier = pickle.load(f)

    def _predict_tweets(self):
        for raw in self.raw_tweets:
            clean_tweet = process_tweet(raw)

    def process_tweets(self):
        pass

    def _classify(self, cleaned_tweet):
        self._politics_classifier.predict()
