from ident.db.connection import conn
from ident.db.queries.session import get_session_info_by_token_hash

from ident.db.models import Session, User
from secrets import token_urlsafe


def lookup(
    value: str, 
    load_user: bool = False, 
    load_session: bool = False
) -> tuple[Session | None, User | None]:
    # TODO: hash value

    res = get_session_info_by_token_hash(
        conn, 
        value, 
        load_user=load_user,
        load_session=load_session
    )

    if res is None:
        return (None, None)
    
    return res

def verify_totp_code(
    code: int,
    secret: str
):
    pass

def get_context(id: str) -> int: 
    pass

def make_context(user_id: int) -> str:
    return token_urlsafe(20)