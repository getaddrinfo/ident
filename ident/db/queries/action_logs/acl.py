import fdb
from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogFieldChange,
    ActionLogActor,

    ActionAclCreated,
    ActionAclUpdated,
    ActionAclDeleted
)

@fdb.transactional
def add_create_acl_entry(
    tr,
    acl_id: int,
    actor: ActionLogActor,
    changes: list[ActionLogFieldChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=acl_id,
        acl_created=ActionAclCreated(changes=changes)
    ))

@fdb.transactional
def add_delete_acl_entry(
    tr,
    acl_id: int,
    actor: ActionLogActor
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=acl_id,
        acl_deleted=ActionAclDeleted()
    ))

@fdb.transactional
def add_update_acl_entry(
    tr,
    acl_id: int,
    actor: ActionLogActor,
    changes: list[ActionLogFieldChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=acl_id,
        acl_updated=ActionAclUpdated(changes=changes)
    ))