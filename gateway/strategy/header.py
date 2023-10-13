from .base import BaseStrategy

class HeaderStrategy(BaseStrategy):
    name: str

    def __init__(self, header_name: str):
        self.name = header_name
    
    def get(self, environ) -> str:
        return environ.get(
            f'HTTP_{self.name.upper()}',
            None
        )