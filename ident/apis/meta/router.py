from flask import Blueprint

meta_router = Blueprint('meta', __name__, url_prefix='/meta')

from ident.lib.response import returns
from ident.lib.inject import inject

from . import models, service, responses


@meta_router.get("")
@returns(responses.GetMeta)
@inject
def get_meta():
    return service.get()