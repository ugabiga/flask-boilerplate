from core.entities.authentication import Authentication
from core.repositories.authentication import AuthenticationRepository


def create_test_data(repo: AuthenticationRepository) -> Authentication:
    expected_auth = Authentication(
        user_id=1,
        category=Authentication.EMAIL,
        identification="test@test.com",
        secret="some_hash_value",
    )
    repo.create_auth(expected_auth)
    return expected_auth


def test_success_find_authentication(repo: AuthenticationRepository) -> None:
    expected_auth = create_test_data(repo)

    target_auth = repo.find_auth(Authentication.EMAIL, "test@test.com")

    assert target_auth is not None
    assert target_auth.user_id == expected_auth.user_id


def test_fail_find_authentication(repo: AuthenticationRepository) -> None:
    create_test_data(repo)

    target_auth = repo.find_auth(Authentication.EMAIL, "atest@test.com")
    assert target_auth is None
