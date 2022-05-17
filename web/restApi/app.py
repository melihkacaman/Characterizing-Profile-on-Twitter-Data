from flask import Flask, request, jsonify
from apis.twitter_api import get_user_information

app = Flask(__name__)


@app.route('/user/<id>', methods=['GET'])
def home(id):
    result = get_user_information(id)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
