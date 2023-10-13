import time
from math import floor

from json import dumps
from base64 import urlsafe_b64encode

from nacl.signing import SigningKey

# TODO: source this from config instead
key = SigningKey.generate()


def build_headers(environ, identity = None):
    headers = filter(
        _filter_headers,
        environ.items()
    )

    headers = map(
        _map_headers,
        headers
    )

    # to dict
    headers = { key: value for (key, value) in headers }

    current_user = _encode_base64_for_header(dumps(identity or None))
    current_timestamp = floor(time.time() * 1000)

    headers['x-ident-current-user'] = current_user
    headers['x-ident-current-timestamp'] = current_timestamp
    headers['x-ident-ed25519-signature'] = _sign(current_timestamp, current_user)

    return headers

def _sign(now: int, data: bytes):
    sign_source = f'{now}:{data}'
    signed = key.sign(bytes(sign_source, "utf-8"))

    return _encode_hex_for_header(signed.signature)

def _encode_base64_for_header(raw) -> str:
    return urlsafe_b64encode(
        raw if isinstance(raw, bytes) else bytes(raw, "utf-8")
    ).decode("utf-8").rstrip("=")

def _encode_hex_for_header(raw) -> str:
    raw = raw if isinstance(raw, bytes) else bytes(raw, "utf-8")

    return raw.hex()

def _filter_headers(raw):
    (key, _) = raw
    return key.startswith("HTTP_")

def _map_headers(raw):
    (key, value) = raw

    key: str = key

    key = key \
        .removeprefix("HTTP_") \
        .replace("_", "-") \
        .lower()
    
    return (key, value)