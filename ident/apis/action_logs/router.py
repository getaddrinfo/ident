from flask import Blueprint

action_logs_router = Blueprint('action_logs', __name__, url_prefix='/action_logs')

from ident.lib.validation import validate
from ident.lib.inject import inject
from ident.lib.response import returns
from ident.lib.error.internal import InternalServerError


from google.protobuf.message import Message

from ident.db.diff import try_unwind

from . import models, service, responses

@action_logs_router.get("")
@validate(query=models.ListActionLogsQueryParams)
def list_action_logs():
    pass

@action_logs_router.get("/<entry_id>")
@validate(path=models.GetActionLogEntryPathParams)
@returns(responses.GetActionLog)
@inject
def get_action_log(path: models.GetActionLogEntryPathParams):
    (it, actor) = service.get(path.entry_id)
    (type, value) = unpack(it)

    if value is None:
        raise InternalServerError()

    return responses.GetActionLog(
        id=it.id,
        type=type,
        data=responses.ActionLogData(
            target_id=it.target_id,
            actor=responses.ActionLogActorUser(
                id=actor.id,
                email=actor.email,
                username=actor.username
            ),
            **responses.ActionLogData.unwind(value)
        )
    )

@action_logs_router.get("/create")
def create():
    it = service.demo()
    return "OK"

def unpack(log: Message) -> tuple[str, Message]:
    key = log.WhichOneof("action")
    
    if key is None:
        return (None, None)

    return (key, getattr(log, key))