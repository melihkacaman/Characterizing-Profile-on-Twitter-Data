import tweepy as tw
from templates.profile import Profile
from common.error import Error
from common.result_back import Result

# constants
API_KEY = 'B7Y17gCCAfTe515xuZwGhuVlH'
API_KEY_SECRET = '1lGo5GPcilwKzNy4SVGbgleI285oTK0zF2TAAKbb69vj6PFu3n'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKALawEAAAAAEv7yYYtpXWXx6fv24Q9I4DnzqMg%3DEtLytFqguYLOAE8aSrFVmkK28FWlTGlKJ9PutxDf0QgGsGg8sX'
BEARER_TOKEN2 = 'AAAAAAAAAAAAAAAAAAAAAKALawEAAAAAswdCYqqlZc1l%2BY1nOh7zYn2GaW4%3DA6vVrRYXf8JtlKVkbdok2Ej5m174CQskMQi2MOL8fUaTdby5uL'
ACCESS_TOKEN = '1440392138697547777-ZbNqj8Vz27k9mk4s009V76REekQpoY'
ACCESS_TOKEN_SECRET = 'ik2qalQeHpdw5cbU6QNtqZl2HYnmDVRQ1cRPbv9WPpywu'


def get_user_information(user_name: str):
    usernames = Client.get_instance().get_users(usernames=[user_name])
    result = None
    if usernames.data is not None:
        result = Result(Profile(usernames.data[0].id, usernames.data[0].name, usernames.data[0].username))
    else:
        result = Result(None, Error('Not Found the User that you gave', 'User Not Found'))

    return result


def get_user_recent_tweets(username: str):
    user = get_user_information(username)
    if not user.exist_error():
        tweet_list = []
        for tweet in tw.Paginator(Client.get_instance().get_users_tweets, id=user.result_object.user_id,
                                  max_results=100,
                                  tweet_fields=['lang']).flatten(limit=1000):
            if tweet.lang == 'en' or tweet.lang == 'EN':
                tweet_list.append(tweet.text)
        return Result({
            'tweet_list': tweet_list
        }, None)
    else:
        return Result(None, Error("Username not found", 'User Not Found'))


class Client:
    __instance = None

    @staticmethod
    def get_instance():
        if Client.__instance is None:
            Client()

        return Client.__instance

    def __init__(self):
        if Client.__instance is None:
            Client.__instance = tw.Client(bearer_token=BEARER_TOKEN2)
