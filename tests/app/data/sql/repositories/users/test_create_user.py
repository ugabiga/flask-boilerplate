from app.data.sql.repositories.users import UserSQLRepository


def test_create_user(repo: UserSQLRepository) -> None:
    expected_nickname = "sample"
    user = repo.create_user(expected_nickname)

    assert user.id > 0
    assert user.nickname == expected_nickname
