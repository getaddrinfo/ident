import fdb
from ..connection import groups, group_members

from .user import get_user

from typing import Optional
from ident.db.buf.user_pb2 import User

import time, math

def now_snowflake():
    now = math.floor(time.time() * 1000)

    return now << 22

@fdb.transactional
def remove_member(tr, group_id, user_id):
    del tr[groups.pack((group_id,user_id))]

@fdb.transactional
def add_member(tr, group_id, user_id):
    tr[groups.pack((group_id,user_id))] = b''

# TODO: handle last_user_id = None
# TODO: pagination
# TODO: finish implementation
@fdb.transactional
def list_members(
    tr, 
    group_id, 
    limit: int,
    last_user_id: Optional[int] = None,
):
    out = []

    start = group_members.pack((
        group_id,0
    )) if last_user_id is None else group_members.pack((
        group_id,
        last_user_id
    ))

    for k, _ in tr.get_range(
        fdb.KeySelector.first_greater_than(start),
        fdb.KeySelector.first_greater_than(group_members.pack((group_id, now_snowflake()))),
        limit=limit
    ):
        (_, _, member_id) = fdb.tuple.unpack(k)
        out.append(member_id)


    has_more = has_more_members(tr, group_id, out[-1]) if len(out) > 0 else False

    return [get_user(tr, member_id) for member_id in out], has_more

@fdb.transactional
def has_more_members(
    tr,
    group_id,
    member_id
):
    start = group_members.pack((group_id, member_id))
    end = group_members.pack((group_id, now_snowflake()))

    maybe_next = tr.get_range(
        fdb.KeySelector.first_greater_than(start), 
        fdb.KeySelector.first_greater_than(end), 
        limit=1
    )

    has_more = False

    # TODO: is there a better way of doing this?
    for _, _ in maybe_next:
        has_more = True

    return has_more


@fdb.transactional
def count_members(tr, group_id) -> int:
    return len(tr[groups.range((group_id,))])