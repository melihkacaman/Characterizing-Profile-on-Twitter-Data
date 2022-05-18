from flask import Flask, request, jsonify
from apis.twitter_api import get_user_information, get_user_recent_tweets
from classifiers.classifier_manager import ClassifierManager

app = Flask(__name__)
classifie = ClassifierManager()

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    return jsonify(get_user_information(id).result_object)


@app.route('/user/<id>/tweets', methods=['GET'])
def get_tweets(id):
    result = get_user_recent_tweets(id)

    return jsonify(result.result_object)


if __name__ == '__main__':
    app.run()
