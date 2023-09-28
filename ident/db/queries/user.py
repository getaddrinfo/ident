import fdb
from typing import Optional

from ..connection import users, user_email_idx
from ident.db.buf.user_pb2 import User

from ..exceptions.uniqueness import UniqueConstraintViolationError


@fdb.transactional
def get_user(tr, user_id) -> Optional[User]:
    data = tr[users.pack((user_id,))]

    if data == None:
        return None

    return User.FromString(bytes(data))

@fdb.transactional
def create_user(tr, user: User):
    if not is_unique_email(tr, user.email):
        raise UniqueConstraintViolationError('user_email')
    

    set_user(tr, user)
    set_user_email_idx(tr, user.email, user.id)
    
@fdb.transactional
def set_user(tr, user: User):
    packed = user.SerializeToString()

    tr[users.pack((user.id,))] = packed

@fdb.transactional
def remove_user(tr, user_id: int):
    # used to clean up the index
    user = get_user(tr, user_id)

    # remove the email index
    del tr[user_email_idx.pack((user.email,))]
    
    # TODO: remove group memberships

    del tr[users.pack((user_id,))]

@fdb.transactional
def is_unique_email(tr, email: str):
    return tr[user_email_idx.pack((email,))] == None

def set_user_email_idx(tr, email: str, id: int):
    tr[user_email_idx.pack((email,))] = fdb.tuple.pack((id,))