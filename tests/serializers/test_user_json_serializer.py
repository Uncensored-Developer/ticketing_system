import json
import uuid
from ticketing_system.serializers.user_json_serializer import UserJsonEncoder
from ticketing_system.domain.user import User


def test_serialize_user_model():
    token = uuid.uuid4().hex
    email = 'xxx@yyy.com'
    user_type = 'customer'
    name = 'Jane Doe'

    user = User(token, email, user_type, name)

    expected_json = """
        {{
            "token": "{}",
            "email": "{}",
            "user_type": "{}",
            "name": "{}"
        }}
    """.format(token, email, user_type, name)

    json_user = json.dumps(user, cls=UserJsonEncoder)

    assert json.loads(json_user) == json.loads(expected_json)

