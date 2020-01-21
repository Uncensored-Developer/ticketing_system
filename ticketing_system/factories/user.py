from ticketing_system.repository.memrepo.user_repo import UserRepo as UserMemRepo
from ticketing_system.repository.postgres_repo.user_repo import UserRepo
from ticketing_system.use_cases.user_use_cases import UserListUseCase
from ticketing_system.serializers.user_json_serializer import UserJsonEncoder


def create_user_memrepo(data):
    return UserMemRepo(data)


def create_user_repo():
    return UserRepo()


def create_user_list_use_case(data):
    return UserListUseCase(repo=create_user_memrepo(data))


def create_user_json_encoder():
    return UserJsonEncoder
