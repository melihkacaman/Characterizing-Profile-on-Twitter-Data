from flask import Flask, request, jsonify, session
from apis.twitter_api import get_user_information, get_user_recent_tweets
from classifiers.classifier_manager import Classifier

app = Flask(__name__)


# todo: deprecate it.
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    result = get_user_information(id)
    if not result.exist_error():
        return jsonify(result.result_object.__dict__)
    else:
        return jsonify(result.error.__dict__)


@app.route('/user/<id>/tweets', methods=['GET'])
def get_tweets(id):
    result = get_user_recent_tweets(id)
    if not result.exist_error():
        return jsonify(result.result_object)
    else:
        return jsonify(result.error.__dict__)


@app.route('/user/<id>/predict', methods=['GET'])
def get_results(id):
    tweet_list_result = get_user_recent_tweets(id)
    if not tweet_list_result.exist_error():
        res = tweet_list_result.result_object
        manager = Classifier(res['tweet_list'])
        actual_result, json_result = manager.process_tweets()
        return json_result

    else:
        return jsonify(tweet_list_result.error)


if __name__ == '__main__':
    app.run()
