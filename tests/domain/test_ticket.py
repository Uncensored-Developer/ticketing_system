import uuid
from ticketing_system.domain.ticket import Ticket
from ticketing_system.domain.user import User


def test_ticket_model_init():
    user = User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow')
    subject = 'TEST TEST TEST'
    dept = 'sales'
    priority = 'low'
    msg = 'lorem ipsum'
    code = uuid.uuid4().hex[:5]

    ticket = Ticket(
        user=user, subject=subject, department=dept,
        priority=priority, message=msg, code=code
    )

    assert ticket.user == user
    assert ticket.subject == subject
    assert ticket.department == dept
    assert ticket.priority == priority
    assert ticket.message == msg
    assert ticket.code == code


def test_ticket_model_from_dict():
    user = User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow')
    subject = 'TEST TEST TEST'
    dept = 'sales'
    priority = 'low'
    msg = 'lorem ipsum'
    code = uuid.uuid4().hex[:5]

    ticket = Ticket.from_dict({
        'user': user,
        'subject': subject,
        'department': dept,
        'priority': priority,
        'message': msg,
        'code': code
    })

    assert ticket.user == user
    assert ticket.subject == subject
    assert ticket.department == dept
    assert ticket.priority == priority
    assert ticket.message == msg
    assert ticket.code == code


def test_ticket_model_to_dict():
    user = User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow')
    subject = 'TEST TEST TEST'
    dept = 'sales'
    priority = 'low'
    msg = 'lorem ipsum'
    code = uuid.uuid4().hex[:5]

    ticket_dict = {
        'user': user,
        'subject': subject,
        'department': dept,
        'priority': priority,
        'message': msg,
        'code': code,
        'closed': False,
        'created_at': None,
        'updated_at': None
    }

    ticket = Ticket.from_dict(ticket_dict)

    assert ticket.to_dict() == ticket_dict


def test_ticket_model_comparison():
    user = User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow')
    subject = 'TEST TEST TEST'
    dept = 'sales'
    priority = 'low'
    msg = 'lorem ipsum'
    code = uuid.uuid4().hex[:5]

    ticket_dict = {
        'user': user,
        'subject': subject,
        'department': dept,
        'priority': priority,
        'message': msg,
        'code': code
    }

    ticket1 = Ticket.from_dict(ticket_dict)
    ticket2 = Ticket.from_dict(ticket_dict)

    assert ticket1 == ticket2
