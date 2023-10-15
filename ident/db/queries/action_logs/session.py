import fdb

from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogFieldChange,

    ActionSessionCreated
)



@fdb.transactional
def add_session_created_entry(
    tr,
    actor: ActionLogActor,
    session_id: int,
    changes: list[ActionLogFieldChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=session_id,
        session_created=ActionSessionCreated(changes=changes)
    ))
