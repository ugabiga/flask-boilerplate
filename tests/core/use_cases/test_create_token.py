from unittest import mock
from unittest.mock import Mock

import jwt

from core.entities.authentication import Authentication
from core.helpers.encrypt import EncryptHelper
from core.use_cases.authentications.create_token import (
    CreateTokenDto,
    CreateTokenUseCase,
)


def create_mock_repo(user_id: int) -> Mock:
    repo = mock.Mock()
    repo.find_auth.return_value = Authentication(
        user_id,
        Authentication.EMAIL,
        "test@test.com",
        EncryptHelper().encode("some_secret"),
    )
    return repo


def test_create_token() -> None:
    user_id = 1
    category = Authentication.EMAIL
    identification = "test@test.com"
    secret = "some_secret"

    repo = create_mock_repo(user_id)
    dto = CreateTokenDto(
        category=category, identification=identification, secret=secret
    )
    output = CreateTokenUseCase(repo).execute(dto)

    assert output.is_success()

    decoded_token = jwt.decode(output.get_data(), algorithms="HS256")
    assert decoded_token["user_id"] == user_id
