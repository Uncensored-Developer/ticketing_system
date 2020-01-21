import collections
from .request_objects import ValidRequestObject, InvalidRequestObject


class ListRepliesRequestObject(ValidRequestObject):

    accepted_filters = ['ticket', ]

    def __init__(self, filters=None, user=None):
        self.filters = filters
        self.user = user
        self.data = filters

    @classmethod
    def from_dict(cls, adict, user=None):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict:
            if not isinstance(adict['filters'], collections.Mapping):
                invalid_req.add_error('filters', 'filters should be a mapping')
                return invalid_req

            for k, v in adict['filters'].items():
                if k not in cls.accepted_filters:
                    invalid_req.add_error(
                        'filters', 'key {} cannot be used'.format(k)
                    )
        if not user:
            invalid_req.add_error('Authentication', 'not authenticated')
        if invalid_req.has_errors():
            return invalid_req
        return cls(filters=adict.get('filters', None), user=user)
