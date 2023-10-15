from flask import Blueprint

action_logs_router = Blueprint('action_logs', __name__, url_prefix='/action_logs')

from ident.lib.validation import validate

from . import models, service

@action_logs_router.get("")
@validate(query=models.ListActionLogsQueryParams)
def list_action_logs():
    pass

@action_logs_router.get("/<entry_id>")
@validate(path=models.GetActionLogEntryPathParams)
def get_action_log():
    pass