from ident.lib.response import define

@define
class Group:
    id: str
    name: str

@define
class User:
    id: str
    username: str
    avatar_url: str
    email: str
    attributes: dict[str, str]

@define
class Member:
    user: User
