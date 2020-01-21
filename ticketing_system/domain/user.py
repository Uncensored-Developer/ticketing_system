from .base import Base


class User(Base):

    def __init__(self, token, email, user_type, name):
        self.token = token
        self.email = email
        self.user_type = user_type
        self.name = name

    @classmethod
    def from_dict(cls, adict):
        return cls(
            token=adict['token'],
            email=adict['email'],
            user_type=adict['user_type'],
            name=adict['name']
        )

    def to_dict(self):
        return {
            'token': self.token,
            'email': self.email,
            'user_type': self.user_type,
            'name': self.name
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
