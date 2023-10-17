import fdb

from ._handler import insert_entry

from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogChange,

    ActionNetworkCreated,
    ActionNetworkUpdated,
    ActionNetworkDeleted
)


@fdb.transactional
def add_network_created_entry(
    tr,
    actor: ActionLogActor,
    network_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=network_id,
        network_created=ActionNetworkCreated(changes=changes)
    ))

@fdb.transactional
def add_network_updated_entry(
    tr,
    actor: ActionLogActor,
    network_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=network_id,
        network_updated=ActionNetworkUpdated(changes=changes)
    ))

@fdb.transactional
def add_network_deleted_entry(
    tr,
    actor: ActionLogActor,
    network_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=network_id,
        network_deleted=ActionNetworkDeleted()
    ))