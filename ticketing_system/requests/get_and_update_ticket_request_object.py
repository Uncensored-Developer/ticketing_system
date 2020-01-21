import collections
from .request_objects import ValidRequestObject, InvalidRequestObject


class GetAndUpdateTicketRequestObject(ValidRequestObject):

    accepted_filters = ['code', 'closed']

    def __init__(self, filters=None, user=None):
        self.filters = filters
        self.user = user

    @classmethod
    def from_dict(cls, adict, user=None):
        invalid_req = InvalidRequestObject()

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('code', 'adict should be a mapping')
            return invalid_req

        for k, v in adict.items():
            if k not in cls.accepted_filters:
                invalid_req.add_error(
                    'params', 'key {} cannot be used'.format(k)
                )
        if not user:
            invalid_req.add_error('Authentication', 'not authenticated')
        if invalid_req.has_errors():
            return invalid_req
        return cls(filters=adict, user=user)
