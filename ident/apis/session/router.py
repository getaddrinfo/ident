from flask import Blueprint

from ident.lib.response import returns
from ident.lib.validation import validate
from ident.lib.inject import inject

from . import models, service, responses

sessions_router = Blueprint('sessions', __name__, url_prefix='/sessions')

@sessions_router.post('/login')
@validate(body=models.LoginBody)
@returns(responses.LoginResult)
@inject
def login(data: models.LoginBody):
    return responses.LoginResultMust2FA(
        context_id=service.make_context(0)
    )

@sessions_router.post('/mfa')
@validate(body=models.Mfa)
@returns(responses.LoginResult)
@inject
def mfa(body: models.Mfa):
    ctx = service.get_context(body.context_id)

    service.verify_totp_code(
        body.code,
        ctx
    )
    
    return models.LoginResultComplete(
        token='test'
    )