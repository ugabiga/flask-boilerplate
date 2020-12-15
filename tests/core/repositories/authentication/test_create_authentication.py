from core.entities.authentication import Authentication
from core.repositories.authentication import AuthenticationRepository


def test_create_authentication(repo: AuthenticationRepository) -> None:
    expected_auth = Authentication(
        user_id=1,
        category=Authentication.EMAIL,
        identification="test@test.com",
        secret="some_hash_value",
    )
    new_auth = repo.create_auth(expected_auth)
    assert expected_auth == new_auth
