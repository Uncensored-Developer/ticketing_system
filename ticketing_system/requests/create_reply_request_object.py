import collections
from .request_objects import ValidRequestObject, InvalidRequestObject


class CreateReplyRequestObject(ValidRequestObject):

    accepted_params = ['user', 'ticket', 'message', ]

    def __init__(self, data=None, user=None):
        self.data = data
        self.user = user

    @classmethod
    def from_dict(cls, adict, user=None):
        invalid_req = InvalidRequestObject()

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('adict', 'adict should be a mapping')
            return invalid_req

        for k, v in adict.items():
            if k not in cls.accepted_params:
                invalid_req.add_error(k, 'Invalid attribute {}'.format(k))

        if not user:
            invalid_req.add_error('Authentication', 'not authenticated')

        if invalid_req.has_errors():
            return invalid_req
        return cls(data=adict, user=user)
