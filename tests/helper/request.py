import json
from typing import Dict

from flask import Response
from flask.testing import FlaskClient


class ResponseHelper:
    def __init__(self, response: Response) -> None:
        self._response = response

    def get_data(self) -> Dict:
        return json.loads(self._response.data.decode("utf-8"))

    def get_status_code(self) -> int:
        return self._response.status_code


class RequestClient:
    def __init__(self, client: FlaskClient) -> None:
        self._client = client

    def get(self, url: str = "") -> ResponseHelper:
        resp = self._client.get(url, content_type="application/json")
        return ResponseHelper(resp)
