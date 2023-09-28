from cattrs import Converter

from ...types.ip import IPv4Address, IPv6Address, IPAddress

def _unstructure_ip_address(value: IPAddress) -> str:
    return str(value)

def apply(conv: Converter):
    conv.register_unstructure_hook(IPv4Address, _unstructure_ip_address)
    conv.register_unstructure_hook(IPv6Address, _unstructure_ip_address)