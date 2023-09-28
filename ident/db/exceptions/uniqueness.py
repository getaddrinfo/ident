from .base import BaseDatabaseError

class UniqueConstraintViolationError(BaseDatabaseError):
    def __init__(
        self,
        idx: str
    ) -> None:
        super().__init__(
            f'uniqueness violated on constraint {idx}'
        )