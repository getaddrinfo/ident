from typing import Protocol


class BaseStrategy(Protocol):
    def get(self, environ) -> str:
        ... 