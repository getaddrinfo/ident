from ident.lib.response import Paginable, define, union, unstructurer, to_serialized_form
from ident.lib.response.types import Snowflake

from ident.db.diff import try_unwind

from google.protobuf.json_format import MessageToDict


from typing import Any

@define
class ActionLogActorSystem:
    pass

@define
class ActionLogActorUser:
    id: Snowflake
    username: str
    email: str

@define
class ActionLogActorApiUser:
    id: Snowflake
    owner: ActionLogActorUser

ActionLogActor = ActionLogActorSystem | ActionLogActorUser | ActionLogActorApiUser


# get self
@define
class ActionLogData:
    target_id: Snowflake
    actor: ActionLogActor
    changes: Any | None
    unstructured: dict[str, Any]

    @staticmethod
    def unstructure(data: 'ActionLogData'):
        as_dict = {
            "target_id": to_serialized_form(data.target_id, from_=Snowflake),
            "actor": to_serialized_form(data.actor, from_=ActionLogActor),
            **data.unstructured
        }

        if data.changes is not None:
            as_dict["changes"] = data.changes

        return as_dict
    
    @staticmethod
    def unwind(value):
        unwound = try_unwind(value)
        data = MessageToDict(value)

        if unwound is not None:
            data.pop("changes")

        return {
            "unstructured": data,
            "changes": unwound
        }

@define
class GetActionLog:
    id: Snowflake
    type: str
    data: ActionLogData
    
@define
class ListActionLog(Paginable[GetActionLog]):
    pass


union(
    ActionLogActor,
    tag='type',
    mapping={
        'user': ActionLogActorUser,
        'system': ActionLogActorSystem,
        'api': ActionLogActorApiUser
    }
)

unstructurer(
    ActionLogData,
    ActionLogData.unstructure
)