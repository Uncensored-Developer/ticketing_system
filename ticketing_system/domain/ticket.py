from .base import Base


class Ticket(Base):

    def __init__(
        self, user, subject, department, priority,
        message, code=None, closed=False, created_at=None, updated_at=None
    ):
        self.user = user
        self.subject = subject
        self.department = department
        self.priority = priority
        self.message = message
        self.code = code
        self.closed = closed
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, adict):
        return cls(
            user=adict['user'],
            subject=adict['subject'],
            department=adict['department'],
            priority=adict['priority'],
            message=adict['message'],
            code=adict['code'],
            created_at=adict.get('created_at', None),
            updated_at=adict.get('updated_at', None),
            closed=adict.get('closed', False)
        )

    def to_dict(self):
        return {
            'user': self.user,
            'subject': self.subject,
            'department': self.department,
            'priority': self.priority,
            'message': self.message,
            'code': self.code,
            'closed': self.closed,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
