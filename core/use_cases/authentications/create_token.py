import inject

from core.repositories.authentication import AuthenticationRepository


class CreateTokenUseCase:
    @inject.autoparams()
    def __init__(self, repository: AuthenticationRepository) -> None:
        self.__repository = repository

    def execute(self, category: str, identification: str, secret: str):
        self.__repository.find_auth(category, identification, secret)
