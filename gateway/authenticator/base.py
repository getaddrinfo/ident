from typing import Protocol

from .models import Application, PolicyExecutionResult

class AuthenticatorProtocol(Protocol):
    def find_application(self, environ) -> Application:
        ...

    def can_access(self, auth: str) -> PolicyExecutionResult:
        ...