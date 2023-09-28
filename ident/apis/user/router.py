from flask import Blueprint

from ident.lib.response import returns
from ident.lib.validation import validate
from ident.lib.middleware import authenticate
from ident.lib.inject import inject

from ident.db.models import User

from . import models, responses, service

user_router = Blueprint('users', __name__, url_prefix="/users")

@user_router.get("/@me")
@authenticate
@returns(responses.GetSelf)
@inject
def get_self(current_user: User, b: User):
    return responses.GetSelf(
        id=str(current_user.id)
    )


@user_router.post("")
@validate(body=models.CreateUser)
@returns(responses.CreateUser)
@inject
def create_user(body: models.CreateUser):
    created = service.create(body)   

    return responses.CreateUser(
        id=str(created.id)
    )

@user_router.get("/<id>")
@validate(path=models.GetUserPathParams)
@returns(responses.GetUser)
@inject
def get_user_by_id(params: models.GetUserPathParams):
    user = service.get(params.id)
        
    return responses.GetUser(
        id=user.id,
        username=user.username,
        email=user.email,
        avatar_url=None if user.avatar_url == "" else user.avatar_url,
        attributes=user.attributes
    )

@user_router.delete("/<id>")
@validate(path=models.DeleteUserPathParams)
@inject
def delete_user_by_id(params: models.DeleteUserPathParams):
    service.delete(params.id)

    # return a 204 response
    return "", 204