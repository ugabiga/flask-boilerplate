from unittest import mock

from core.entities.authentication import Authentication
from core.helpers.encrypt import EncryptHelper
from core.use_cases.authentications.create_token import (
    CreateTokenDto,
    CreateTokenUseCase,
)
from core.use_cases.authentications.validate_token import ValidateTokenUseCase


def create_token(user_id: int) -> str:
    user_id = user_id
    category = Authentication.EMAIL
    identification = "test@test.com"
    secret = "some_secret"

    repo = mock.Mock()
    repo.find_auth.return_value = Authentication(
        user_id,
        Authentication.EMAIL,
        "test@test.com",
        EncryptHelper().encode("some_secret"),
    )

    dto = CreateTokenDto(
        category=category, identification=identification, secret=secret
    )

    output = CreateTokenUseCase(repo).execute(dto)

    return output.get_data()


def test_validate_token() -> None:
    target_user_id = 1
    token = create_token(target_user_id)
    result = ValidateTokenUseCase().execute(token)
    assert result.is_success
    assert target_user_id == result.get_data()["user_id"]
