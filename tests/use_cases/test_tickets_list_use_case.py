import pytest
import uuid
from unittest import mock
from ticketing_system.domain.ticket import Ticket
from ticketing_system.domain.user import User
from ticketing_system.use_cases.ticket_use_cases import ListTicketsUseCase


@pytest.fixture
def domain_tickets():
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
    domain_users = [user_1, user_2, user_3]

    return [
        Ticket(
            user=user,
            subject='TWEST',
            department='sales',
            priority='low',
            message='lorem ipsum',
            code=uuid.uuid4().hex[:5]
        )
        for user in domain_users
    ]


# def test_tickets_list_without_parameters(domain_tickets):
#     repo = mock.Mock()
#     repo.list.return_value = domain_tickets
#
#     ticket_list_use_case = TicketListUseCase(repo)
#     result = ticket_list_use_case.execute()
#
#     repo.list.assert_called_with()
#
#     assert result == domain_tickets
