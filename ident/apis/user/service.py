from ident.db.models import User, UserType
from ident.db.connection import conn
import ident.db.queries.user as queries

from .models import CreateUser
from ident.db.exceptions import UniqueConstraintViolationError

from ident.lib.error.user import UnknownUser, EmailAlreadyExists


def get(id: int) -> User:
    user = queries.get_user(conn, id)
    
    if user == None:
        raise UnknownUser()

    return user


def create(user: CreateUser) -> User:
    model = User(
        id=1,
        type=UserType.UTUser,
        avatar_url="",
        email=user.email,
        attributes=user.attributes,
        username=user.username
    )

    try:
        queries.create_user(conn, model)
        return model
    except UniqueConstraintViolationError:
        raise EmailAlreadyExists()
    
def delete(id: int) -> bool:
    queries.remove_user(conn, id)
    return True