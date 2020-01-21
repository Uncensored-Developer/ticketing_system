import json
from .user_json_serializer import UserJsonEncoder


class TicketJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'user': UserJsonEncoder().default(o.user),
                'subject': o.subject,
                'department': o.department,
                'priority': o.priority,
                'message': o.message,
                'code': o.code,
                'closed': o.closed,
                'created_at': str(o.created_at),
                'updated_at': o.updated_at
            }
            if o.updated_at:
                to_serialize['updated_at'] = str(o.updated_at)
            return to_serialize
        except AttributeError:
            return super().default(o)
