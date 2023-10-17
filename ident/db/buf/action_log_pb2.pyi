from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
IGNORED_FIELD_NUMBER: _ClassVar[int]
ignored: _descriptor.FieldDescriptor

class ActionAclCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionAclDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionAclUpdated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionApplicationAccessed(_message.Message):
    __slots__ = ["ipv4", "ipv6"]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    ipv4: int
    ipv6: bytes
    def __init__(self, ipv4: _Optional[int] = ..., ipv6: _Optional[bytes] = ...) -> None: ...

class ActionApplicationCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionApplicationDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionGroupCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionGroupDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionGroupMemberAdded(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: int
    def __init__(self, member_id: _Optional[int] = ...) -> None: ...

class ActionGroupMemberRemoved(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class ActionGroupUpdated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionLog(_message.Message):
    __slots__ = ["acl_created", "acl_deleted", "acl_updated", "actor", "application_accessed", "application_created", "application_deleted", "group_created", "group_deleted", "group_member_added", "group_member_removed", "group_updated", "id", "network_created", "network_deleted", "network_updated", "session_created", "target_id", "user_created", "user_deleted", "user_password_changed", "user_suspended", "webhook_created", "webhook_deleted", "webhook_updated"]
    ACL_CREATED_FIELD_NUMBER: _ClassVar[int]
    ACL_DELETED_FIELD_NUMBER: _ClassVar[int]
    ACL_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ACCESSED_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_CREATED_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_DELETED_FIELD_NUMBER: _ClassVar[int]
    GROUP_CREATED_FIELD_NUMBER: _ClassVar[int]
    GROUP_DELETED_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMBER_ADDED_FIELD_NUMBER: _ClassVar[int]
    GROUP_MEMBER_REMOVED_FIELD_NUMBER: _ClassVar[int]
    GROUP_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CREATED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_DELETED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_UPDATED_FIELD_NUMBER: _ClassVar[int]
    SESSION_CREATED_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CREATED_FIELD_NUMBER: _ClassVar[int]
    USER_DELETED_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_CHANGED_FIELD_NUMBER: _ClassVar[int]
    USER_SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_CREATED_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_DELETED_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_UPDATED_FIELD_NUMBER: _ClassVar[int]
    acl_created: ActionAclCreated
    acl_deleted: ActionAclDeleted
    acl_updated: ActionAclUpdated
    actor: ActionLogActor
    application_accessed: ActionApplicationAccessed
    application_created: ActionApplicationCreated
    application_deleted: ActionApplicationDeleted
    group_created: ActionGroupCreated
    group_deleted: ActionGroupDeleted
    group_member_added: ActionGroupMemberAdded
    group_member_removed: ActionGroupMemberRemoved
    group_updated: ActionGroupUpdated
    id: int
    network_created: ActionNetworkCreated
    network_deleted: ActionNetworkDeleted
    network_updated: ActionNetworkUpdated
    session_created: ActionSessionCreated
    target_id: int
    user_created: ActionUserCreated
    user_deleted: ActionUserDeleted
    user_password_changed: ActionUserPasswordChanged
    user_suspended: ActionUserSuspended
    webhook_created: ActionWebhookCreated
    webhook_deleted: ActionWebhookDeleted
    webhook_updated: ActionWebhookUpdated
    def __init__(self, id: _Optional[int] = ..., target_id: _Optional[int] = ..., actor: _Optional[_Union[ActionLogActor, _Mapping]] = ..., acl_created: _Optional[_Union[ActionAclCreated, _Mapping]] = ..., acl_updated: _Optional[_Union[ActionAclUpdated, _Mapping]] = ..., acl_deleted: _Optional[_Union[ActionAclDeleted, _Mapping]] = ..., application_created: _Optional[_Union[ActionApplicationCreated, _Mapping]] = ..., application_accessed: _Optional[_Union[ActionApplicationAccessed, _Mapping]] = ..., application_deleted: _Optional[_Union[ActionApplicationDeleted, _Mapping]] = ..., group_created: _Optional[_Union[ActionGroupCreated, _Mapping]] = ..., group_updated: _Optional[_Union[ActionGroupUpdated, _Mapping]] = ..., group_member_added: _Optional[_Union[ActionGroupMemberAdded, _Mapping]] = ..., group_member_removed: _Optional[_Union[ActionGroupMemberRemoved, _Mapping]] = ..., group_deleted: _Optional[_Union[ActionGroupDeleted, _Mapping]] = ..., network_created: _Optional[_Union[ActionNetworkCreated, _Mapping]] = ..., network_updated: _Optional[_Union[ActionNetworkUpdated, _Mapping]] = ..., network_deleted: _Optional[_Union[ActionNetworkDeleted, _Mapping]] = ..., session_created: _Optional[_Union[ActionSessionCreated, _Mapping]] = ..., user_created: _Optional[_Union[ActionUserCreated, _Mapping]] = ..., user_suspended: _Optional[_Union[ActionUserSuspended, _Mapping]] = ..., user_password_changed: _Optional[_Union[ActionUserPasswordChanged, _Mapping]] = ..., user_deleted: _Optional[_Union[ActionUserDeleted, _Mapping]] = ..., webhook_created: _Optional[_Union[ActionWebhookCreated, _Mapping]] = ..., webhook_updated: _Optional[_Union[ActionWebhookUpdated, _Mapping]] = ..., webhook_deleted: _Optional[_Union[ActionWebhookDeleted, _Mapping]] = ...) -> None: ...

class ActionLogActor(_message.Message):
    __slots__ = ["id", "type"]
    class ActionLogActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ActionLogActorAPIKey: ActionLogActor.ActionLogActorType
    ActionLogActorSystem: ActionLogActor.ActionLogActorType
    ActionLogActorUser: ActionLogActor.ActionLogActorType
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: ActionLogActor.ActionLogActorType
    def __init__(self, type: _Optional[_Union[ActionLogActor.ActionLogActorType, str]] = ..., id: _Optional[int] = ...) -> None: ...

class ActionLogChange(_message.Message):
    __slots__ = ["field", "key"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    field: ActionLogFieldChange
    key: ActionLogKeyChange
    def __init__(self, field: _Optional[_Union[ActionLogFieldChange, _Mapping]] = ..., key: _Optional[_Union[ActionLogKeyChange, _Mapping]] = ...) -> None: ...

class ActionLogFieldChange(_message.Message):
    __slots__ = ["after", "before", "key"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    after: _any_pb2.Any
    before: _any_pb2.Any
    key: str
    def __init__(self, before: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., after: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class ActionLogKeyChange(_message.Message):
    __slots__ = ["after", "before", "key"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    after: _any_pb2.Any
    before: _any_pb2.Any
    key: str
    def __init__(self, before: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., after: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class ActionNetworkCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionNetworkDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionNetworkUpdated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionSessionCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionUserCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionUserDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionUserPasswordChanged(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionUserSuspended(_message.Message):
    __slots__ = ["note"]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: str
    def __init__(self, note: _Optional[str] = ...) -> None: ...

class ActionWebhookCreated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...

class ActionWebhookDeleted(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ActionWebhookUpdated(_message.Message):
    __slots__ = ["changes"]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[ActionLogChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[ActionLogChange, _Mapping]]] = ...) -> None: ...
