from core.repositories.users import UserRepository


def test_create_user(repo: UserRepository) -> None:
    expected_nickname = "sample"
    user = repo.create_user(expected_nickname)

    assert user.id > 0
    assert user.nickname == expected_nickname
