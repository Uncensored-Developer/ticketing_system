from .base import Base


class Reply(Base):

    def __init__(self, ticket, user, message, created_at):
        self.ticket = ticket
        self.user = user
        self.message = message
        self.created_at = created_at

    @classmethod
    def from_dict(cls, adict):
        return cls(
            ticket=adict['ticket'],
            user=adict['user'],
            message=adict['message'],
            created_at=adict['created_at'],
        )

    def to_dict(self):
        return {
            'ticket': self.ticket,
            'user': self.user,
            'message': self.message,
            'created_at': self.created_at
        }
