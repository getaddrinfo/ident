from flask import Blueprint

from ident.lib.validation import validate
from ident.lib.response import returns

from . import models, service

webhooks_router = Blueprint('webhooks', __name__, url_prefix='/webhooks')

@webhooks_router.post("")
@validate(body=models.CreateWebhook)
def create_webhook(body: models.CreateWebhook):
    pass