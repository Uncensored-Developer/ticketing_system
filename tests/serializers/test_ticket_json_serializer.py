import json
import uuid
from ticketing_system.serializers.ticket_json_serializer import TicketJsonEncoder
from ticketing_system.serializers.user_json_serializer import UserJsonEncoder
from ticketing_system.domain.user import User
from ticketing_system.domain.ticket import Ticket


def test_serialize_ticket_model():
    user = User(uuid.uuid4().hex, 'abc@gmail.com', 'customer', 'jerry dow')
    subject = 'TEST TEST TEST'
    dept = 'sales'
    priority = 'low'
    msg = 'lorem ipsum'
    code = uuid.uuid4().hex[:5]

    ticket = Ticket(
        user=user, subject=subject, department=dept,
        priority=priority, message=msg, code=code,
        created_at='5684747476'
    )

    expected_json = """
        {{
            "user": {},
            "subject": "{}",
            "department": "{}",
            "priority": "{}",
            "message": "{}",
            "code": "{}",
            "closed": {},
            "created_at": "5684747476",
            "updated_at": null
        }}
    """.format(json.dumps(user, cls=UserJsonEncoder),
               subject, dept, priority, msg, code, "false")

    json_ticket = json.dumps(ticket, cls=TicketJsonEncoder)

    assert json.loads(json_ticket) == json.loads(expected_json)
