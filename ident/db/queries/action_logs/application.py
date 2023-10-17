import fdb
import ipaddress

from ._handler import insert_entry

from ident.db.models import (
    ActionLogActor,
    ActionLogChange,
    ActionLog,

    ActionApplicationCreated,
    ActionApplicationAccessed,
    ActionApplicationDeleted
)


@fdb.transactional
def add_application_create_entry(
    tr,
    application_id: int,
    actor: ActionLogActor,
    props: list[ActionLogChange]
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=application_id,
        application_created=ActionApplicationCreated(changes=props)
    ))

@fdb.transactional
def add_application_access_entry(
    tr,
    application_id: int,
    actor: ActionLogActor,
    source_ipv4: ipaddress.IPv4Address | None = None,
    source_ipv6: ipaddress.IPv6Address | None = None
):
    access_log = ActionApplicationAccessed()

    if source_ipv4 is not None:
        access_log.ipv4 = int(source_ipv4)

    if source_ipv6 is not None:
        access_log.ipv6 = bytes(source_ipv6)

    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=application_id,
        application_accessed=access_log
    ))

@fdb.transactional
def add_application_delete_entry(
    tr,
    application_id: int,
    actor: ActionLogActor
):
    insert_entry(tr, ActionLog(
        actor=actor,
        target_id=application_id,
        application_deleted=ActionApplicationDeleted()
    ))