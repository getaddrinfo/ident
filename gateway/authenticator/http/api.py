from .http import HTTP
from ..models import Application, PolicyExecutionResult

import json


class API:
    http: HTTP

    def __init__(self, token: str):
        self.http = HTTP(token)

    def get_application_by_host(self, *, host: str) -> Application:
        url = f'/v1/applications/host/{host}'
        res = self.http.get(url)

        data = res.json()

        return Application(**data)
        
    def execute_policy(self, *, application_id: int, user_id: int) -> PolicyExecutionResult:
        url = f'/v1/policies/execute'
        body = { 'user_id': str(user_id), 'application_id': str(application_id) }

        res = self.http.post(url, headers={ 'Content-Type': 'application/json' }, data=json.dumps(body))

        body = res.json()

        return PolicyExecutionResult(**body)
