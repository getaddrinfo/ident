__all__ = ("IPNetwork", "IPAddress", "IPv4Address", "IPv6Address", "IPv4Network", "IPv6Network")

from ipaddress import (
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Network
)

IPAddress = IPv4Address | IPv6Address
IPNetwork = IPv4Network | IPv6Network