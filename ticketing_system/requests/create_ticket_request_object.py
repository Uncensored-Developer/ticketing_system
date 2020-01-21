import collections
from .request_objects import ValidRequestObject, InvalidRequestObject


class CreateTicketRequestObject(ValidRequestObject):

    accepted_params = ['user', 'subject', 'department', 'priority', 'message', 'code']
    priority = ['low', 'medium', 'high']
    department = ['sales', 'security', 'technical']

    def __init__(self, data=None, user=None):
        self.data = data
        self.user = user
        self.filters = data

    @classmethod
    def from_dict(cls, adict, user=None):
        invalid_req = InvalidRequestObject()

        if not isinstance(adict, collections.Mapping):
            invalid_req.add_error('adict', 'adict should be a mapping')
            return invalid_req

        for k, v in adict.items():
            if k not in cls.accepted_params:
                invalid_req.add_error(k, 'Invalid attribute {}'.format(k))

            if k == 'priority' and v not in cls.priority:
                invalid_req.add_error('priority', 'Invalid value for attribute {}'.format(k))

            if k == 'department' and v not in cls.department:
                invalid_req.add_error('department', 'Invalid value for attribute {}'.format(k))

        if not user:
            invalid_req.add_error('Authentication', 'not authenticated')

        if invalid_req.has_errors():
            return invalid_req
        return cls(data=adict, user=user)
