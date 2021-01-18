from core.entities.authentication import Authentication
from core.repositories.authentication import AuthenticationRepository
from core.repositories.users import UserRepository
from tests.helper.request import RequestClient


# noinspection PyUnusedLocal
def test_call_index(
    client: RequestClient,
    user_repo: UserRepository,
    auth_repo: AuthenticationRepository,
) -> None:
    request_auth_category = "email"
    request_auth_identification = "sample_id"
    request_auth_secret = "123456"

    # Create user and authentication
    user = user_repo.create_user("sample")
    auth_repo.create_auth(
        Authentication(
            user_id=user.id,
            category=request_auth_category,
            identification=request_auth_identification,
            secret=request_auth_secret,
        )
    )

    resp = client.post(
        "/v1/authentications",
        {
            "category": request_auth_category,
            "identification": request_auth_identification,
            "secret": request_auth_secret,
        },
    )

    assert resp.get_status_code() == 200
    assert resp.get_data()
