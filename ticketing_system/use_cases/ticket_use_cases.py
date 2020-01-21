from abc import ABC, abstractmethod
from ticketing_system.responses.response_objects import ResponseSuccess, ResponseFailure


class AbstractTicketUseCase(ABC):

    def __init__(self, ticket_repo, user_repo):
        self.ticket_repo = ticket_repo
        self.user_repo = user_repo

    def execute(self, request_obj):
        if not request_obj:
            return ResponseFailure.build_from_invalid_request_object(request_obj)
        try:
            import copy
            user = self.user_repo.get(token=request_obj.user)
            filters = copy.deepcopy(request_obj.filters)
            if not user:
                return ResponseFailure.build_resource_error(
                    message='Invalid auth token.'
                )
            if user.user_type == 'customer':
                filters.update({'user': user})
            return self.operation1(self.ticket_repo, filters, user=user)
        except Exception as e:
            return ResponseFailure.build_system_error(
                "{}: {}".format(e.__class__.__name__, "{}".format(e)))

    @abstractmethod
    def operation1(self, ticket_repo, data, user=None):
        pass


class ListTicketsUseCase(AbstractTicketUseCase):

    def operation1(self, ticket_repo, data, **kwargs):
        tickets = self.ticket_repo.list(filters=data)
        return ResponseSuccess(tickets)


class GetTicketUseCase(AbstractTicketUseCase):

    def operation1(self, ticket_repo, data, **kwargs):
        ticket = self.ticket_repo.get(filters=data)
        if not ticket:
            return ResponseFailure.build_resource_error(
                message='Ticket not found among yours.'
            )
        return ResponseSuccess(ticket)


class CreateTicketUseCase(AbstractTicketUseCase):

    def operation1(self, ticket_repo, data, user=None):
        import uuid
        data.update({
            'code': uuid.uuid4().hex[:5],
            'user': user
        })
        print(data)
        ticket = self.ticket_repo.create(data=data)
        return ResponseSuccess(ticket)


class UpdateTicketUseCase(AbstractTicketUseCase):

    def operation1(self, ticket_repo, data, user=None):
        ticket = self.ticket_repo.update(data=data)
        if not ticket:
            return ResponseFailure.build_resource_error(
                message='Ticket not found among yours.'
            )
        return ResponseSuccess(ticket)
