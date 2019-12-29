from unittest import mock

from app.core.dtos.users import CreateUserDto
from app.core.entities.users import User
from app.core.use_cases.create_users import CreateUserUseCase


def test_create_user() -> None:
    expected_user = User(1, "user_nickname")

    dto = CreateUserDto("user_nickname")
    repo = mock.Mock()
    repo.create_user.return_value = expected_user

    result = CreateUserUseCase(repo, dto).execute()
    assert result == expected_user
