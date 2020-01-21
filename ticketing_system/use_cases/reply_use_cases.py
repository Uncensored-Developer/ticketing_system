from ticketing_system.responses.response_objects import ResponseSuccess, ResponseFailure
from abc import ABC, abstractmethod


class AbstractReplyUseCase(ABC):

    def __init__(self, reply_repo, user_repo, ticket_repo):
        self.reply_repo = reply_repo
        self.user_repo = user_repo
        self.ticket_repo = ticket_repo

    def execute(self, request_obj):
        if not request_obj:
            return ResponseFailure.build_from_invalid_request_object(request_obj)
        try:
            import copy
            data = copy.deepcopy(request_obj.data)
            user = self.user_repo.get(token=request_obj.user)
            ticket = self.ticket_repo.get({'code': data['ticket']})
            if not user:
                return ResponseFailure.build_resource_error(
                    message='Invalid auth token.'
                )
            if not ticket:
                return ResponseFailure.build_resource_error(
                    message='Ticket not found.'
                )
            if user == 'customer':
                user_ticket = self.ticket_repo.get({'code': data['ticket'], 'user': user})
                if not user_ticket:
                    return ResponseFailure.build_resource_error(
                        message='You are not allowed on this ticket.'
                    )

            # TODO
            return self.operation1(user=user, ticket=ticket, data=data)
        except Exception as e:
            return ResponseFailure.build_system_error(
                "{}: {}".format(e.__class__.__name__, "{}".format(e)))

    @abstractmethod
    def operation1(self, *args, **kwargs):
        pass


class CreateReplyUseCase(AbstractReplyUseCase):

    def operation1(self, *args, **kwargs):
        user = kwargs.get('user', None)
        data = kwargs.get('data', None)
        ticket = kwargs.get('ticket', None)

        if user and data and ticket:
            data.update({'user': user})
            data['ticket'] = ticket
            reply = self.reply_repo.create(data)
            if ticket.closed:
                self.ticket_repo.update({'code': ticket.code, 'closed': False})
            return ResponseSuccess(reply)


class ListRepliesUseCase(AbstractReplyUseCase):

    def operation1(self, *args, **kwargs):
        user = kwargs.get('user', None)
        data = kwargs.get('data', None)
        ticket = kwargs.get('ticket', None)
        if user and data and ticket:
            replies = self.reply_repo.list({'ticket': ticket})
            return ResponseSuccess(replies)
