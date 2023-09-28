from cattrs import Converter

from . import bytes, ip_address, ip_network, snowflake

def apply_to(conv: Converter):
    bytes.apply(conv)
    ip_address.apply(conv)
    ip_network.apply(conv)
    snowflake.apply(conv)