from cattrs import Converter

from ...types.ip import IPv4Network, IPv6Network


def _unstructure_ip_network(value):
    return str(value)

def apply(conv: Converter):
    conv.register_structure_hook(
        IPv4Network,
        _unstructure_ip_network
    )

    conv.register_structure_hook(
        IPv6Network,
        _unstructure_ip_network
    )