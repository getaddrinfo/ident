from ipaddress import (
    IPv4Address, IPv6Address
)

from ident.db.connection import conn
from ident.db.models import (
    Application, 
    ActionLogActor, 
    Group,
    NetworkPolicy,
    Session,
    User,
    Webhook
)

from ident.db.queries.action_logs import (
    acl as acl_action_log_queries,
    application as application_action_log_queries,
    group as group_action_log_queries,
    network as network_action_log_queries,
    session as session_action_log_queries,
    user as user_action_log_queries,
    webhook as webhook_action_log_queries
)

from enum import Enum
from dataclasses import dataclass

class ActorType(Enum):
    user = 0
    system = 1
    api = 2

    __mappings = {
        user: ActionLogActor.ActionLogActorUser,
        system: ActionLogActor.ActionLogActorSystem,
        api: ActionLogActor.ActionLogActorAPIKey
    }

    def to_proto(self) -> ActionLogActor.ActionLogActorType:
        return self.__mappings[self]

@dataclass
class Actor:
    """
    A dataclass representing an Actor (user, the system, an api call) within an
    action. Ideally should be constructed via the staticmethods `user`, `system` and `api`, e.g.,
    
    ```py
    service.on_acl_delete(
        Actor.user(current_user.id),
        acl.id
    )
    ```

    These are converted to protobuf values, and used when fetching action logs to lookup the underlying resource
    (user, api key) that actioned them, or represent it as a system action
    """

    id: int
    type: ActorType

    @staticmethod
    def user(id):
        return Actor(id=id, type=ActorType.user)
    
    @staticmethod
    def system(id):
        return Actor(id=0, type=ActorType.system)
    
    @staticmethod
    def api(id):
        return Actor(id=id, type=ActorType.api)
    
    def to_proto(self) -> ActionLogActor:
        return ActionLogActor(
            id=self.id,
            type=self.type.to_proto()
        )

"""
TODO: implement the diffing from before -> after on protobufs.

We know that there is the `__slots__` field that exists on all of these classes,
so maybe we can write a generic implementation that is just like `protobuf.diff(before, after) -> list[ActionLogFieldChange]`

where:
`protobuf.diff(before, after) -> list[ActionLogFieldChange]` `(field=field, before=value before, after=value after)`
`protobuf.diff(None, after) -> list[ActionLogFieldChange]` `(field=field, before=None, after=value)`

and unchanges values are removed from the final list (or not added in first place)

potential issues:
- nested values
- ADTs (lists, maps)

"""

# acls
def on_acl_create(
    *,
    actor: Actor,
    acl # TODO: type
):
    raise NotImplementedError("on_acl_create/2: not implemented")

    acl_action_log_queries.add_create_acl_entry(
        conn,
        acl.id,
        actor.to_proto(),
        []
    )

# TODO: changes
def on_acl_update(
    *,
    actor: Actor,
    acl_id: int
):
    raise NotImplementedError("on_acl_update/2: not implemented")

    acl_action_log_queries.add_update_acl_entry(
        conn,
        acl_id,
        actor.to_proto(),
        []
    )

def on_acl_delete(
    *,
    actor: Actor,
    acl_id: int,
):
    raise NotImplementedError("on_acl_delete/2: not implemented")

    acl_action_log_queries.add_delete_acl_entry(
        conn,
        acl_id,
        actor.to_proto()
    )


# application
def on_application_create(
    *,
    actor: Actor,
    application: Application
):
    application_action_log_queries.add_application_create_entry(
        conn,
        application.id,
        actor.to_proto(),
        []
    )

def on_application_access(
    *,
    actor: Actor,
    application_id: int,
    source: IPv4Address | IPv6Address
):
    ipv4 = None
    ipv6 = None

    if isinstance(source, IPv4Address):
        ipv4 = source
    
    if isinstance(source, IPv6Address):
        ipv6 = source

    assert ipv4 is not None and ipv6 is not None, "ipv4/ipv6 must be set by now"

    application_action_log_queries.add_application_access_entry(
        conn,
        application_id,
        actor.to_proto(),
        source_ipv4=ipv4,
        source_ipv6=ipv6
    )

def on_application_delete(
    *,
    actor: Actor,
    application_id: int
):
    application_action_log_queries.add_application_delete_entry(
        conn,
        application_id,
        actor.to_proto()
    )


# group
def on_group_create(
    *,
    actor: Actor,
    group: Group
):
    group_action_log_queries.add_group_created_entry(
        conn,
        actor.to_proto(),
        group.id,
        []
    )

def on_group_member_add(
    *,
    actor: Actor,
    group_id: int,
    added_member_id: int
):
    group_action_log_queries.add_group_member_add_entry(
        conn,
        actor.to_proto(),
        group_id,
        added_member_id
    )

def on_group_member_remove(
    *,
    actor: Actor,
    group_id: int,
    removed_member_id: int
):
    group_action_log_queries.add_group_member_remove_entry(
        conn,
        actor.to_proto(),
        group_id,
        removed_member_id
    )

def on_group_update(
    *,
    actor: Actor,
    before: Group,
    after: Group
):
    group_action_log_queries.add_group_updated_entry(
        conn,
        actor.to_proto(),
        after.id,
        []
    )

def on_group_delete(
    *,
    actor: Actor,
    group_id: int
):
    group_action_log_queries.add_group_deleted_entry(
        conn,
        actor.to_proto(),
        group_id
    )


# network
def on_network_create(
    *,
    actor: Actor,
    network: NetworkPolicy
):
    network_action_log_queries.add_network_created_entry(
        conn,
        actor.to_proto(),
        network.id,
        []
    )

def on_network_update(
    *,
    actor: Actor,
    before: NetworkPolicy,
    after: NetworkPolicy
):
    network_action_log_queries.add_network_deleted_entry(
        conn,
        actor.to_proto(),
        after.id,
        []
    )

def on_network_delete(
    *,
    actor: Actor,
    network_id: int
):
    network_action_log_queries.add_network_deleted_entry(
        conn,
        actor.to_proto(),
        network_id
    )


# sessions
def on_session_create(
    *,
    actor: Actor,
    session: Session
):
    session_action_log_queries.add_session_created_entry(
        conn,
        actor.to_proto(),
        session.id,
        []
    )

# users
def on_user_create(
    *,
    actor: Actor,
    user: User
):
    user_action_log_queries.add_user_created_entry(
        conn,
        actor.to_proto(),
        user.id,
        []
    )

def on_user_suspend(
    *,
    actor: Actor,
    suspended_user_id: int,
    note: str | None 
):
    user_action_log_queries.add_user_suspended_entry(
        conn,
        actor.to_proto(),
        suspended_user_id,
        note
    )

def on_user_password_change(
    *,
    actor: Actor,
    changed_user_id: int
):
    user_action_log_queries.add_user_password_changed_entry(
        conn,
        actor.to_proto(),
        changed_user_id
    )

def on_user_delete(
    *,
    actor: Actor,
    deleted_user_id: int
):
    user_action_log_queries.add_user_deleted_entry(
        conn,
        actor.to_proto(),
        deleted_user_id
    )


# webhooks
def on_webhook_create(
    *,
    actor: Actor,
    webhook: Webhook
):
    webhook_action_log_queries.add_webhook_created_entry(
        conn,
        actor.to_proto(),
        webhook.id,
        []
    )
    

def on_webhook_update(
    *,
    actor: Actor,
    before: Webhook,
    after: Webhook
):
    webhook_action_log_queries.add_webhook_updated_entry(
        conn,
        actor.to_proto(),
        after.id,
        []
    )


def on_webhook_delete(
    *,
    actor: Actor,
    webhook_id: int,
):
    webhook_action_log_queries.add_webhook_deleted_entry(
        conn,
        actor.to_proto(),
        webhook_id
    )