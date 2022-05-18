import json


class Profile:
    def __init__(self, user_id, name, username):
        self.user_id = user_id
        self.name = name
        self.username = username

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
