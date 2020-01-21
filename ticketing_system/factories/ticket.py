from ticketing_system.repository.postgres_repo.ticket_repo import TicketRepo
from ticketing_system.use_cases.ticket_use_cases import (
    ListTicketsUseCase, CreateTicketUseCase, GetTicketUseCase,
    UpdateTicketUseCase,
)
from ticketing_system.serializers.ticket_json_serializer import TicketJsonEncoder
from .user import create_user_repo


def create_ticket_repo():
    return TicketRepo()


def create_ticket_list_use_case():
    return ListTicketsUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo()
    )


def create_ticket_use_case():
    return CreateTicketUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo()
    )


def create_get_ticket_use_case():
    return GetTicketUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo()
    )


def create_update_ticket_use_case():
    return UpdateTicketUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo()
    )


def create_ticket_json_encoder():
    return TicketJsonEncoder
