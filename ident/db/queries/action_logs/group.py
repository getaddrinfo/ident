import fdb

from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogFieldChange,

    ActionGroupCreated,
    ActionGroupDeleted,
    ActionGroupMemberAdded,
    ActionGroupMemberRemoved,
    ActionGroupUpdated
)


@fdb.transactional
def add_group_created_entry(
    tr,
    group_id: int,
    actor: ActionLogActor,
    props: list[ActionLogFieldChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=group_id,
        group_created=ActionGroupCreated(changes=props)
    ))

@fdb.transactional
def add_group_updated_entry(
    tr,
    actor: ActionLogActor,
    group_id: int,
    changes: list[ActionLogFieldChange]    
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=group_id,
        group_updated=ActionGroupUpdated(changes=changes)
    ))

@fdb.transactional
def add_group_member_add_entry(
    tr,
    actor: ActionLogActor,
    group_id: int,
    member_id: int,
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=group_id,
        group_member_added=ActionGroupMemberAdded(member_id=member_id)
    ))

@fdb.transactional
def add_group_member_remove_entry(
    tr,
    actor: ActionLogActor,
    group_id: int,
    user_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=group_id,
        group_member_removed=ActionGroupMemberRemoved(user_id=user_id)
    ))

@fdb.transactional
def add_group_deleted_entry(
    tr,
    actor: ActionLogActor,
    group_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=group_id,
        group_deleted=ActionGroupDeleted()
    ))