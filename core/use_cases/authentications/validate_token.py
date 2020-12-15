from typing import Dict

import jwt

from core.use_cases.output import Output, Success


class ValidateTokenUseCase:
    def execute(self, token: str) -> Output[Dict[str, int]]:
        decoded_token = jwt.decode(token)
        return Success(decoded_token)
