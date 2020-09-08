from unittest import mock

from core.entities.authentication import Authentication
from core.use_cases.authentications.create_token import CreateTokenUseCase
from core.use_cases.authentications.validate_token import ValidateTokenUseCase


def create_token(user_id: int) -> str:
    target_auth = Authentication(
        user_id=user_id,
        category=Authentication.EMAIL,
        identification="test@test.com",
        secret="some_secret",
    )
    repo = mock.Mock()
    repo.find_auth.return_value = Authentication(
        target_auth.user_id,
        target_auth.category,
        target_auth.identification,
        target_auth.secret,
    )
    result = CreateTokenUseCase(repo).execute(
        target_auth.category, target_auth.identification, target_auth.secret
    )
    return result.get_data()


def test_validate_token() -> None:
    target_user_id = 1
    token = create_token(target_user_id)
    result = ValidateTokenUseCase().execute(token)
    assert result.is_success
    assert target_user_id == result.get_data()["user_id"]
