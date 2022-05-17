import tweepy as tw

# constants
API_KEY = 'B7Y17gCCAfTe515xuZwGhuVlH'
API_KEY_SECRET = '1lGo5GPcilwKzNy4SVGbgleI285oTK0zF2TAAKbb69vj6PFu3n'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKALawEAAAAAEv7yYYtpXWXx6fv24Q9I4DnzqMg%3DEtLytFqguYLOAE8aSrFVmkK28FWlTGlKJ9PutxDf0QgGsGg8sX'
BEARER_TOKEN2 = 'AAAAAAAAAAAAAAAAAAAAAKALawEAAAAAswdCYqqlZc1l%2BY1nOh7zYn2GaW4%3DA6vVrRYXf8JtlKVkbdok2Ej5m174CQskMQi2MOL8fUaTdby5uL'
ACCESS_TOKEN = '1440392138697547777-ZbNqj8Vz27k9mk4s009V76REekQpoY'
ACCESS_TOKEN_SECRET = 'ik2qalQeHpdw5cbU6QNtqZl2HYnmDVRQ1cRPbv9WPpywu'


def get_user_information(user_name):
    usernames = Client.get_instance().get_users(usernames=[user_name])
    if usernames.data is not None:
        return {
            'user_id': usernames.data[0].id,
            'name': usernames.data[0].name,
            'user_name': usernames.data[0].username
        }
    else:
        return {
            'user_id': None,
            'name': None,
            'user_name': None
        }


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
