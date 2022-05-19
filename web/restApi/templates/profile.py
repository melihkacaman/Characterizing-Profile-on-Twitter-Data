import json


class Profile:
    def __init__(self, user_id, name, username, created_year, description, location, url, image_url):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.created_year = created_year
        self.description = description
        self.location = location
        self.url = url
        self.image_url = image_url

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
