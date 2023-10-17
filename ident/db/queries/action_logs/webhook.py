import fdb

from ._handler import insert_entry


from ident.db.models import (
    ActionLog,
    ActionLogActor,
    ActionLogChange,

    ActionWebhookCreated,
    ActionWebhookUpdated,
    ActionWebhookDeleted
)


@fdb.transactional
def add_webhook_created_entry(
    tr,
    actor: ActionLogActor,
    webhook_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=webhook_id,
        webhook_created=ActionWebhookCreated(changes=changes)
    ))

@fdb.transactional
def add_webhook_updated_entry(
    tr,
    actor: ActionLogActor,
    webhook_id: int,
    changes: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=webhook_id,
        webhook_updated=ActionWebhookUpdated(changes=changes)
    ))

@fdb.transactional
def add_webhook_deleted_entry(
    tr,
    actor: ActionLogActor,
    webhook_id: int
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_Id=webhook_id,
        webhook_deleted=ActionWebhookDeleted()
    ))