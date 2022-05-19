import pickle
import numpy as np
from classifiers.utils import *
from templates.tweet import *


class ClassifierManager:
    def __init__(self, tweet_list: list):
        self.raw_tweets = tweet_list
        self._results = {
            TweetLabel.POLITICS: 0.0,
            TweetLabel.FOOD: 0.0,
            TweetLabel.SPORT: 0.0,
            TweetLabel.TECHNOLOGY: 0.0,
            'predicted_tweets': []
        }
        self._initialize_classifiers()
        self._predict_tweets()

    def _initialize_classifiers(self):
        # 1. Politics classifier : linear SVM
        with open('resources/politics_linearSVM2', 'rb') as f:
            self._politics_classifier = pickle.load(f)
        with open('resources/politics_freqs', 'rb') as f:
            self._politics_freqs = pickle.load(f)

        # 2. Food Classifier : Naive Bayes
        with open('resources/food_naivebayes.', 'rb') as f:
            self._food_classifier = pickle.load(f)

        # 3. Sport Classifier : Naive Bayes
        with open('resources/sport_naivebayes.', 'rb') as f:
            self._sport_classifier = pickle.load(f)

        # 4. Technology Classifier : Naive Bayes
        with open('resources/technology_naivebayes_', 'rb') as f:
            self._technology_classifier = pickle.load(f)

    def _predict_tweets(self):
        for raw in self.raw_tweets:
            clean_tweet = process_tweet(raw)
            (label, prob) = self._classify(clean_tweet)
            self._increase_results(Tweet(raw, label, clean_tweet))

    def process_tweets(self):
        n = len(self.raw_tweets)
        for key, value in self._results.items():
            if key != 'predicted_tweets':
                self._results[key] = self._results[key] / n

        return self._results

    def _classify(self, cleaned_tweet):
        # politics
        vector = extract_features(cleaned_tweet, self._politics_freqs)
        result_politics = self._politics_classifier.predict_proba(vector)[0, 1]

        # food
        (logprior_food, loglikelihood_food) = self._food_classifier
        result_food = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_food, loglikelihood_food))

        # sport
        (logprior_sport, loglikelihood_sport) = self._sport_classifier
        result_sport = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_sport, loglikelihood_sport))

        # technology
        (logprior_technology, loglikelihood_technology) = self._technology_classifier
        result_technology = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_technology, loglikelihood_technology))

        probabilities = {
            TweetLabel.POLITICS: result_politics,
            TweetLabel.FOOD: result_food,
            TweetLabel.SPORT: result_sport,
            TweetLabel.TECHNOLOGY: result_technology
        }

        # pick the biggest one
        result = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
        return list(result.items())[0]

    def _increase_results(self, predicted_tweet: Tweet):
        self._results[predicted_tweet.predicted_label] += 1
        self._results['predicted_tweets'].append(predicted_tweet)
