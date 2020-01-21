from ticketing_system.repository.postgres_repo.reply_repo import ReplyRepo
from ticketing_system.use_cases.reply_use_cases import CreateReplyUseCase, ListRepliesUseCase
from ticketing_system.serializers.reply_json_serializer import ReplyJsonEncoder
from .ticket import create_ticket_repo
from .user import create_user_repo


def create_reply_repo():
    return ReplyRepo()


def create_reply_use_case():
    return CreateReplyUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo(),
        reply_repo=create_reply_repo()
    )


def create_list_replies_use_case():
    return ListRepliesUseCase(
        ticket_repo=create_ticket_repo(),
        user_repo=create_user_repo(),
        reply_repo=create_reply_repo()
    )


def create_reply_json_serializer():
    return ReplyJsonEncoder
