from .models import (
    CreateApplication, 
    AclTargetType, 
    CreateApplicationAclItemBase,
    CreateApplicationAclItemGroup,
    CreateApplicationAclItemNetworkPolicy,
    CreateApplicationAclItemUser,
    CreateApplicationAclItem
)

from ident.db.connection import conn
import ident.db.queries.acls as queries


def _pick(
    type: AclTargetType,
    property: str,
    acls: list[CreateApplicationAclItem]
):
    return {
        acl[property]: acl.type
        for acl in filter(lambda ty: ty.type == type, acls)
    }

def _is(type: AclTargetType):
    ty = type_to_cls[type]

    def _inner(it):
        return it is ty
    
    return _inner

def create(app: CreateApplication):
    for acl in app.acls:
        _ensure_acl_valid(acl)

    user_ids = _pick(AclTargetType.user, "user_id", app.acls)
    group_ids = _pick(AclTargetType.group, "group_id", app.acls)
    network_policy_ids = _pick(AclTargetType.network_policy, "network_policy_id", app.acls)
    
    queries.create(
        app.name,
        user_ids,
        group_ids,
        network_policy_ids
    )

def _ensure_acl_valid(acl: CreateApplicationAclItemBase):
    validators[acl.target](acl)

def _ensure_group_acl_valid(acl: CreateApplicationAclItemGroup):
    # TOOD: acl.group_id exists
    pass

def _ensure_user_acl_valid(acl: CreateApplicationAclItemUser):
    # TODO: acl.group_id exists
    pass

def _ensure_network_policy_acl_valid(acl: CreateApplicationAclItemNetworkPolicy):
    # TODO: acl.network_policy_id exists
    pass


validators = {
    AclTargetType.group: _ensure_group_acl_valid,
    AclTargetType.network_policy: _ensure_network_policy_acl_valid,
    AclTargetType.user: _ensure_user_acl_valid
}

type_to_cls = {
    AclTargetType.group: CreateApplicationAclItemGroup,
    AclTargetType.network_policy: CreateApplicationAclItemNetworkPolicy,
    AclTargetType.user: CreateApplicationAclItemUser
}