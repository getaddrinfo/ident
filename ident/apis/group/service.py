from ident.db.connection import conn
from attrs import define

import ident.db.queries.groups as queries
from ident.db.models import User

from . import models

@define
class MemberList:
    has_more: bool
    members: list[User]

def list_members(
    id: int,
    last_user_id: int | None,
    limit: int,
) -> MemberList:
    members, has_more = queries.list_members(
        conn,
        id,
        limit,
        last_user_id
    )

    return MemberList(
        has_more=has_more,
        members=list(filter(
            lambda it: it is not None,
            members
        ))
    )