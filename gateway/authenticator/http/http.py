import requests

BASE_API_URL = 'http://localhost:8080'

class HTTP:
    __token: str

    def __init__(self, token: str) -> None:
        self.__token = token

    def get(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None
    ) -> requests.Response:
        return self._call(
            "get",
            url,
            headers=headers
        )
    
    def post(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        body: bytes | str | None = None
    ) -> requests.Response:
        return self._call(
            "post",
            url,
            headers=headers,
            body=body
        )

    def _call(
        self,
        method_name: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        body: bytes | str | None = None,
    ) -> requests.Response:
        return requests.request(
            method_name,
            BASE_API_URL + url,
            headers=self._build_headers(headers),
            data=self._build_body(body)
        )

    def _build_headers(self, headers: dict[str, str] | None):
        if headers is None:
            headers = dict()

        headers['User-Agent'] = 'ident-gateway (https://github.com/getaddrinfo/ident)'
        headers['X-Ident-Gateway-Authorization'] = self.__token

        return headers

    def _build_body(self, body: bytes | str | None):
        if body is None:
            return None

        if isinstance(body, str):
            body = bytes(body, "utf-8")

        return body