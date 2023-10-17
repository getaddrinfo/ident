import fdb

from ident.db.connection import action_logs
from ident.db.models import ActionLog, ActionLogActor
from ident.db.queries.user import get_user

@fdb.transactional
def get(tr, id):
    it = tr[action_logs.pack((id,))]

    if it == None:
        return None

    log = ActionLog.FromString(bytes(it))
    actor = None
    
    if log.actor is not None and log.actor.type == ActionLogActor.ActionLogActorUser:
        actor = get_user(tr, log.actor.id)

    return (log, actor)