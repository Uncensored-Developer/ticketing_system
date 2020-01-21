import pytest
import uuid
from ticketing_system.domain.user import User
from ticketing_system.domain.ticket import Ticket
from ticketing_system.repository.memrepo.user_repo import UserRepo
from ticketing_system.repository.memrepo.ticket_repo import TicketRepo


@pytest.fixture
def user_dicts():
    return [
        {
            'token': uuid.uuid4().hex,
            'email': 'adssghh@hshkj.com',
            'user_type': 'staff',
            'name': 'ken Ten'
        },
        {
            'token': uuid.uuid4().hex,
            'email': 'adssghh@hshkj.com',
            'user_type': 'staff',
            'name': 'ken Ten'
        },
        {
            'token': uuid.uuid4().hex,
            'email': 'adssghh@hshkj.com',
            'user_type': 'staff',
            'name': 'ken Ten'
        }
    ]


@pytest.fixture
def ticket_dicts():
    return [
        {
            'user': User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow'),
            'subject': 'TEST TEST',
            'department': 'technology',
            'priority': 'high',
            'message': 'lorem ipsum',
            'code': uuid.uuid4().hex[:4]
        },
        {
            'user': User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow'),
            'subject': 'TEST TEST',
            'department': 'technology',
            'priority': 'high',
            'message': 'lorem ipsum',
            'code': uuid.uuid4().hex[:4]
        },
        {
            'user': User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow'),
            'subject': 'TEST TEST',
            'department': 'technology',
            'priority': 'high',
            'message': 'lorem ipsum',
            'code': uuid.uuid4().hex[:4]
        }
    ]


def test_user_repo_list(user_dicts):
    repo = UserRepo(user_dicts)
    users = [User.from_dict(i) for i in user_dicts]
    assert repo.list() == users


def test_ticket_repo_list_without_parameters(ticket_dicts):
    repo = TicketRepo(ticket_dicts)
    tickets = [Ticket.from_dict(i) for i in ticket_dicts]
    assert repo.list() == tickets
