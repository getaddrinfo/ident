from ident.lib.response import define

# get self
@define
class GetSelf:
    id: str


@define
class GetUser:
    id: str
    username: str
    email: str
    avatar_url: str | None
    attributes: dict[str, str]


@define
class CreateUser:
    id: str