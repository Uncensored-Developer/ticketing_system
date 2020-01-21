import pytest
import uuid
from unittest import mock
from ticketing_system.domain.user import User
from ticketing_system.use_cases.user_use_cases import UserListUseCase


@pytest.fixture
def domain_users():

    user_1 = User(
        token=uuid.uuid4().hex,
        email='bdsh@gsgsj.com',
        name='Jamie Fox',
        user_type='customer'
    )
    user_2 = User(
        token=uuid.uuid4().hex,
        email='bdsh@gsgsj.com',
        name='Jamie Fox',
        user_type='customer'
    )
    user_3 = User(
        token=uuid.uuid4().hex,
        email='bdsh@gsgsj.com',
        name='Jamie Fox',
        user_type='staff'
    )
    return [user_1, user_2, user_3]


def test_user_list(domain_users):
    repo = mock.Mock()
    repo.list.return_value = domain_users

    user_list_use_case = UserListUseCase(repo)
    result = user_list_use_case.execute()

    repo.list.assert_called_with()

    assert result == domain_users
