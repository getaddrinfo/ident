from gateway.authenticator.models import Application, PolicyExecutionResult
from .base import AuthenticatorProtocol

class FDBAuthenticator(AuthenticatorProtocol):
    def find_application(self, environ) -> Application:
        raise NotImplementedError("FDBAuthorizer.application/1: not implemented")
    
    def can_access(self, auth: str) -> PolicyExecutionResult:
        raise NotImplemented("FDBAuthorizer.can_access/1: not implemented")