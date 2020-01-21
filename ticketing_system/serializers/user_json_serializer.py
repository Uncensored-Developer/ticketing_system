import json


class UserJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'token': o.token,
                'email': o.email,
                'user_type': o.user_type,
                'name': o.name
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
