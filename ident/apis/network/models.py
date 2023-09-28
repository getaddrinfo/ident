from ident.lib.validation import Strict
from ipaddress import IPv4Network


IPNetwork = IPv4Network

class CreateNetwork:
    name: str | None
    cidrs: list[IPNetwork]