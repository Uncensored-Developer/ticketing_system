from ticketing_system.domain.user import User as UserDomain
from .models import User


class UserRepo:

    def get(self, **kwargs):
        return User.query.filter_by(**kwargs).first()
