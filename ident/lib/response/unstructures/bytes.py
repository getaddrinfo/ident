from cattrs import Converter
from base64 import urlsafe_b64encode

def _unstructure_bytes(value: bytes) -> str:
    return str(urlsafe_b64encode(value))

def apply(conv: Converter):
    conv.register_unstructure_hook(bytes, _unstructure_bytes)