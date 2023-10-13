from ..base import AuthenticatorProtocol
from ..models import Application, PolicyExecutionResult
from .api import API

class HttpAuthenticator(AuthenticatorProtocol):
    api: API

    def __init__(self, token: str) -> None:
        self.api = API(token=token)

    def find_application(self, environ) -> Application:
        host = environ.get("HTTP_HOST", None)

        if host is None:
            raise Exception("Cannot idenify host")

        try:  
            return self.api.get_application_by_host(host=host)
        except Exception:
            return None
    
    def can_access(self, *, application_id: int, user_id: int) -> PolicyExecutionResult:
        return self.api.execute_policy(
            application_id=application_id,
            user_id=user_id
        )