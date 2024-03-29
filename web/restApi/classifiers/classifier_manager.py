import pickle
import numpy as np
from classifiers.utils import *
from templates.tweet import *
import json


class _ClassifierManager:
    def __init__(self):
        self._initialize_classifiers()

    def _initialize_classifiers(self):
        # 1. Politics classifier : linear SVM
        with open('resources/politics_linearSVM2', 'rb') as f:
            self.politics_classifier = pickle.load(f)
        with open('resources/politics_freqs', 'rb') as f:
            self.politics_freqs = pickle.load(f)

        # 2. Food Classifier : Naive Bayes
        with open('resources/food_naivebayes.', 'rb') as f:
            self.food_classifier = pickle.load(f)

        # 3. Sport Classifier : Naive Bayes
        with open('resources/sport_naivebayes.', 'rb') as f:
            self.sport_classifier = pickle.load(f)

        # 4. Technology Classifier : Naive Bayes
        with open('resources/technology_naivebayes_', 'rb') as f:
            self.technology_classifier = pickle.load(f)

        # 5. Fitness Classifier : Logistic Regression
        with open('resources/fitness_logisticreg', 'rb') as f:
            self.fitness_classifier = pickle.load(f)

        with open('resources/fitness_freqs', 'rb') as f:
            self.fitness_freqs = pickle.load(f)

        # 6. Magazine Classifier : Naive Bayes
        with open('resources/magazine_naivebayes', 'rb') as f:
            self.magazine_classifier = pickle.load(f)




class ClassifierManagerSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if ClassifierManagerSingleton.__instance is None:
            ClassifierManagerSingleton()

        return ClassifierManagerSingleton.__instance

    def __init__(self):
        if ClassifierManagerSingleton.__instance is None:
            ClassifierManagerSingleton.__instance = _ClassifierManager()


class Classifier:
    def __init__(self, tweet_list: list):
        self.raw_tweets = tweet_list
        self._results = {
            TweetLabel.POLITICS.name: 0.0,
            TweetLabel.FOOD.name: 0.0,
            TweetLabel.SPORT.name: 0.0,
            TweetLabel.TECHNOLOGY.name: 0.0,
            TweetLabel.MAGAZINE.name: 0.0,
            TweetLabel.FITNESS.name: 0.0,
            'predicted_tweets': []
        }

        self._classifier = ClassifierManagerSingleton.get_instance()

    def _predict_tweets(self):
        for raw in self.raw_tweets:
            clean_tweet = process_tweet(raw)
            (label, prob) = self._classify(clean_tweet)
            self._increase_results(Tweet(raw, label, clean_tweet))

    def process_tweets(self):
        self._predict_tweets()
        n = len(self.raw_tweets)
        for key, value in self._results.items():
            if key != 'predicted_tweets':
                self._results[key] = self._results[key] / n
                json_result = self._results.copy()
                json_result['predicted_tweets'] = [item.__dict__ for item in json_result['predicted_tweets']]

        return self._results, json.dumps(json_result)

    def _classify(self, cleaned_tweet):
        # politics
        vector = extract_features(cleaned_tweet, self._classifier.politics_freqs)
        result_politics = self._classifier.politics_classifier.predict_proba(vector)[0, 1]

        # food
        (logprior_food, loglikelihood_food) = self._classifier.food_classifier
        result_food = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_food, loglikelihood_food))

        # sport
        (logprior_sport, loglikelihood_sport) = self._classifier.sport_classifier
        result_sport = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_sport, loglikelihood_sport))

        # technology
        (logprior_technology, loglikelihood_technology) = self._classifier.technology_classifier
        result_technology = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_technology, loglikelihood_technology))

        # magazine
        (logprior_magazine, loglikelihood_magazine) = self._classifier.magazine_classifier
        result_magazine = sigmoid(naive_bayes_predict(cleaned_tweet, logprior_magazine, loglikelihood_magazine))

        # fitness
        result_fitness = self._classifier.fitness_classifier.predict_proba(
            extract_features(cleaned_tweet, self._classifier.fitness_freqs))[0, 1]

        probabilities = {
            TweetLabel.POLITICS: result_politics,
            TweetLabel.FOOD: result_food,
            TweetLabel.SPORT: result_sport,
            TweetLabel.TECHNOLOGY: result_technology,
            TweetLabel.MAGAZINE: result_magazine,
            TweetLabel.FITNESS: result_fitness,
        }

        # pick the biggest one
        result = dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))
        return list(result.items())[0]

    def _increase_results(self, predicted_tweet: Tweet):
        self._results[predicted_tweet.predicted_label.name] += 1
        self._results['predicted_tweets'].append(predicted_tweet)
