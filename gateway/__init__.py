from wsgiref.types import WSGIEnvironment, StartResponse

import json

from .authenticator import AuthenticatorProtocol, HttpAuthenticator
from .strategy import BaseStrategy, CookieStrategy
from .templating import Templating
from . import downstream

auth: AuthenticatorProtocol = HttpAuthenticator('test')
strat: BaseStrategy = CookieStrategy("_ident_tok")
templating = Templating()

def application(
    environ: WSGIEnvironment,
    start_response: StartResponse
):  
    if is_static_read_css(environ):
        # TODO: replace this with a better static file system reader...
        # TODO: cache this
        # TODO: relative imports from current location?
        with open("./gateway/content/static/main.css") as f:
            data = f.read()

        status = '200 OK'
        headers = [('Content-Type', 'text/css'), ('X-Content-Type-Options', 'nosniff')]

        start_response(status, headers)
        return [bytes(data, 'utf-8')]

    if environ.get("PATH_INFO", None) == "/render-403":
        ## these are just example failures for dev
        body = templating.error_variant(
            'forbidden', 
            title='Forbidden',
            description='You do not have the required permissions to access this resource. If you think this is a mistake, contact your administrator.',
            extra={
                'failures': [
                    {
                        'reason': 'Outside of corporate network',
                        'rule': {
                            'id': 1,
                            'name': 'must_be_on_corporate_network'
                        }
                    },
                    {
                        'reason': 'Must be a member of HR',
                        'rule': {
                            'id': 2,
                            'name': 'is_hr'
                        }
                    }
                ]
            }
        )

        status = '403 Forbidden'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        return [body]

    

    body = templating.error(
        title='Not Implemented',
        description='This behaviour is not implemented. If you think this is a mistake, contact your administrator.'
    )
    status = '501 Not Implemented'
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    start_response(status, headers)
    return [body]


def is_static_read_css(environ):
    path = environ.get("PATH_INFO", None)

    if path is None:
        return False
    
    return path == "/__ident_gateway_service__/static/main.css"