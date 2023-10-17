import fdb

from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogChange,

    ActionSessionCreated
)



@fdb.transactional
def add_session_created_entry(
    tr,
    actor: ActionLogActor,
    session_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=session_id,
        session_created=ActionSessionCreated(changes=changes)
    ))
