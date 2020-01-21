from ticketing_system.domain.ticket import Ticket


class TicketRepo:

    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [Ticket.from_dict(i) for i in self.data]

        if filters is None:
            return result
        if 'code' in filters:
            result = [r for r in result if r.code == filters['code']]
        if 'closed' in filters:
            result = [r for r in result if r.closed == filters['closed']]
        if 'department' in filters:
            result = [r for r in result if r.department == filters['department']]
        if 'priority' in filters:
            result = [r for r in result if r.priority == filters['priority']]
        if 'user' in filters:
            result = [r for r in result if r.user == filters['user']]
        return result
