from flask import Blueprint

groups_router = Blueprint('groups', __name__, url_prefix='/groups')

from ident.lib.response import Paginable, returns
from ident.lib.validation import PaginationQueryParams, validate
from ident.lib.inject import inject

from . import models, service, responses

@groups_router.get("")
@returns(Paginable[responses.Group], skip_instance_check=True) # TODO: fix this
@inject
def list_groups():

    return Paginable[models.Group](
        data=[],
        has_more=False,
        url="/groups"
    )


@groups_router.get("/<group_id>/members")
@validate(path=models.ListMembersUrlParams, query=PaginationQueryParams)
@returns(Paginable[responses.Member], skip_instance_check=True)
@inject
def get_group_members(
    params: models.ListMembersUrlParams,
    pagination: PaginationQueryParams
):
    
    res = service.list_members(
        params.group_id,
        pagination.next,
        pagination.limit
    )

    return Paginable[responses.Member](
        url=f"/groups/{params.group_id}/members",
        data=[
            responses.Member(
                user=responses.User(
                    id=user.id,
                    username=user.username,
                    avatar_url=user.avatar_url,
                    email=user.email,
                    attributes=user.attributes
                )
            ) for user in res.members 
        ],
        has_more=res.has_more
    )

@groups_router.put("/<group_id>/members/<user_id>")
@inject
def add_group_member():
    pass

@groups_router.delete("/<group_id>/members/<member_id>")
@inject
def remove_group_member():
    pass