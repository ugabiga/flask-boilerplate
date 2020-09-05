from unittest import mock
from unittest.mock import Mock

import jwt

from core.entities.authentication import Authentication
from core.use_cases.authentications.create_token import CreateTokenUseCase


def create_mock_repo(user_id: int) -> Mock:
    repo = mock.Mock()
    repo.find_auth.return_value = Authentication(
        user_id, Authentication.EMAIL, "test@test.com", "some_secret"
    )
    return repo


def test_create_token() -> None:
    user_id = 1
    category = Authentication.EMAIL
    identification = "test@test.com"
    secret = "some_secret"

    repo = create_mock_repo(user_id)
    output = CreateTokenUseCase(repo).execute(category, identification, secret)
    decoded_token = jwt.decode(output.get_data(), algorithms="HS256")

    assert output.is_success()
    assert decoded_token["user_id"] == user_id
