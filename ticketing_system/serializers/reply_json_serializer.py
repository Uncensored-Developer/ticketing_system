import json
from .user_json_serializer import UserJsonEncoder
from .ticket_json_serializer import TicketJsonEncoder


class ReplyJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'user': UserJsonEncoder().default(o.user),
                'ticket': TicketJsonEncoder().default(o.ticket),
                'message': o.message,
                'created_at': str(o.created_at)
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
