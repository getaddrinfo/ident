from ident.lib.validation import Strict, Lax


# get by id
class GetUserPathParams(Strict):
    id: int


# create
class CreateUser(Strict):
    username: str
    email: str
    attributes: dict[str, str] | None

# delete

class DeleteUserPathParams(Strict):
    id: str