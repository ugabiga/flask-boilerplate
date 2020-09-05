from app.data.sql.repositories.authentication import AuthenticationSQLRepository
from core.entities.authentication import Authentication


def create_test_data(repo: AuthenticationSQLRepository) -> Authentication:
    expected_auth = Authentication(
        user_id=1,
        category=Authentication.EMAIL,
        identification="test@test.com",
        secret="some_hash_value",
    )
    repo.create_auth(expected_auth)
    return expected_auth


def test_success_find_authentication(repo: AuthenticationSQLRepository) -> None:
    expected_auth = create_test_data(repo)

    target_auth = repo.find_auth(
        Authentication.EMAIL, "test@test.com", "some_hash_value"
    )

    assert target_auth is not None
    assert target_auth.user_id == expected_auth.user_id


def test_fail_find_authentication(repo: AuthenticationSQLRepository) -> None:
    create_test_data(repo)

    target_auth = repo.find_auth(
        Authentication.EMAIL, "atest@test.com", "some_hash_value"
    )
    assert target_auth is None
