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

    assert expected_auth.user_id == new_auth.user_id
    assert expected_auth.category == new_auth.category
    assert expected_auth.identification == new_auth.identification
    assert expected_auth.secret != new_auth.secret
