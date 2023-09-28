import fdb

from ident.db.connection import session_idx_token_hash, sessions
from ident.db.queries.user import get_user

from ident.db.models import Session

@fdb.transactional
def get_session_by_id(tr, id: int):
    raw_bytes = tr[sessions.pack((id,))]

    if raw_bytes == None:
        return None
    
    return Session.FromString(raw_bytes)

@fdb.transactional
def get_session_info_by_token_hash(
    tr, 
    hash: str, 
    want_user: bool,
    want_session: bool
):
    lookup = tr[session_idx_token_hash.pack((hash,))]

    if lookup == None:
        return None
    
    (session_id, user_id) = fdb.tuple.unpack(lookup)

    session = get_session_by_id(tr, session_id) if want_session else None

    if session == None and want_session:
        # we are pointing to a dead session? this shouldn't happen
        del tr[session_idx_token_hash.pack((hash,))]
        return None
    
    user = get_user(tr, user_id) if want_user else None
    return (session, user)