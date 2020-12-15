from unittest import mock

from core.entities.authentication import Authentication
from core.entities.users import User
from core.use_cases.users.create_users import CreateUserDto, CreateUserUseCase


def test_create_user() -> None:
    expected_user = User(1, "user_nickname")
    expected_auth = Authentication(
        user_id=expected_user.id,
        category=Authentication.EMAIL,
        identification="user@user.com",
        secret="secret",
    )

    dto = CreateUserDto(
        nickname="user_nickname",
        auth_category=expected_auth.category,
        auth_identification=expected_auth.identification,
        auth_secret=expected_auth.secret,
    )

    user_repo = mock.Mock()
    user_repo.create_user.return_value = expected_user
    auth_repo = mock.Mock()
    auth_repo.create_auth.return_value = expected_auth

    output = CreateUserUseCase(user_repo, auth_repo).execute(dto)
    assert True if output.is_success() else False

    assert output.get_data() == expected_user
    assert output.get_data().authentications[0] == expected_auth
