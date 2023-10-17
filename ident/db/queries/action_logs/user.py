import fdb

from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogChange,

    ActionUserCreated,
    ActionUserPasswordChanged,
    ActionUserSuspended,
    ActionUserDeleted
)


@fdb.transactional
def add_user_created_entry(
    tr,
    actor: ActionLogActor,
    user_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=user_id,
        user_created=ActionUserCreated(changes=changes)
    ))

@fdb.transactional
def add_user_suspended_entry(
    tr,
    actor: ActionLogActor,
    user_id: int,
    note: str
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=user_id,
        user_suspended=ActionUserSuspended(note=note)
    ))

@fdb.transactional
def add_user_password_changed_entry(
    tr,
    actor: ActionLogActor,
    user_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=user_id,
        user_password_changed=ActionUserPasswordChanged()
    ))

@fdb.transactional
def add_user_deleted_entry(
    tr,
    actor: ActionLogActor,
    user_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=user_id,
        user_deleted=ActionUserDeleted()
    ))