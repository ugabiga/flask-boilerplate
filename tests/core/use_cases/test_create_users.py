from unittest import mock

from app.core.entities.authentication import Authentication
from app.core.entities.users import User
from app.core.use_cases.create_users import CreateUserDto
from app.core.use_cases.create_users import CreateUserUseCase


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

    output = CreateUserUseCase(user_repo, auth_repo, dto).execute()

    assert output.get_data() == expected_user
    assert output.get_data().authentications[0] == expected_auth
