import uuid
from ticketing_system.domain.user import User


def test_user_model_init():
    token = uuid.uuid4().hex
    email = 'abce@gmail.com'
    user_type = 'customer'
    name = 'John Doe'
    user = User(token=token, email=email, user_type=user_type, name=name)

    assert user.token == token
    assert user.email == email
    assert user.user_type == user_type
    assert user.name == name


def test_user_model_from_dict():
    token = uuid.uuid4().hex
    email = 'abce@gmail.com'
    user_type = 'customer'
    name = 'John Doe'

    user = User.from_dict({
        'token': token,
        'email': email,
        'user_type': user_type,
        'name': name
    })

    assert user.token == token
    assert user.email == email
    assert user.user_type == user_type
    assert user.name == name


def test_user_model_to_dict():
    user_dict = {
        'token': uuid.uuid4().hex,
        'email': 'xxxx@yyyy.com',
        'user_type': 'customer',
        'name': 'John Doe'
    }
    user = User.from_dict(user_dict)

    assert user.to_dict() == user_dict


def test_user_model_comparison():
    user_dict = {
        'token': uuid.uuid4().hex,
        'email': 'xxxx@yyyy.com',
        'user_type': 'customer',
        'name': 'John Doe'
    }
    user1 = User.from_dict(user_dict)
    user2 = User.from_dict(user_dict)

    assert user1 == user2
