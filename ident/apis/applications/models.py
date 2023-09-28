from enum import StrEnum
from typing import Literal

from ident.lib.validation import Strict, Lax

class AclItemType(StrEnum):
    allow = 'allow'
    deny = 'deny'

class AclTargetType(StrEnum):
    user = 'user'
    group = 'group'
    network_policy = 'network_policy'

class CreateApplicationAclItemBase(Strict):
    type: AclItemType
    target: AclTargetType

class CreateApplicationAclItemUser(CreateApplicationAclItemBase):
    type: Literal[AclTargetType.user]
    user_id: int

class CreateApplicationAclItemGroup(CreateApplicationAclItemBase):
    type: Literal[AclTargetType.group]
    group_id: int

class CreateApplicationAclItemNetworkPolicy(CreateApplicationAclItemBase):
    type: Literal[AclTargetType.network_policy]
    network_policy_id: int

CreateApplicationAclItem = CreateApplicationAclItemUser | CreateApplicationAclItemGroup | CreateApplicationAclItemNetworkPolicy

class CreateApplication(Strict):
    name: str
    acls: list[CreateApplicationAclItem]