from app.core.entities.authentication import Authentication
from app.data.sql.repositories.authentication import AuthenticationSQLRepository


def test_create_authentication(repo: AuthenticationSQLRepository) -> None:
    expected_auth = Authentication(
        user_id=1,
        category=Authentication.EMAIL,
        identification="test@test.com",
        secret="some_hash_value",
    )
    new_auth = repo.create_auth(expected_auth)
    assert expected_auth == new_auth
