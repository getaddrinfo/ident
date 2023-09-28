from flask import Blueprint

networks_router = Blueprint("network", __name__, url_prefix="/networks")

from ident.lib.validation import validate
from ident.lib.id import generate
from ident.lib.inject import inject

from . import service, models


def get_start_end_bounds(network):
    return int(network.network_address + 1), int(network.broadcast_address - 1)

@networks_router.post("")
@validate(body=models.CreateNetwork)
@inject
def create_network(net: models.CreateNetwork):

    return {
        "id": str(generate()),
        "cidrs": {
            str(cidr): get_start_end_bounds(cidr) for cidr in net.cidrs
        }
    }