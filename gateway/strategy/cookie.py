from .base import BaseStrategy

class CookieStrategy(BaseStrategy):
    name: str

    def __init__(self, cookie_name: str) -> None:
        self.name = cookie_name

    def get(self, environ) -> str:
        cookie = environ.get(
            "HTTP_COOKIE",
            None
        )

        # TODO: proper error handling
        if cookie is None:
            raise Exception("no cookie present")
        
        return "HEHE!"
        
