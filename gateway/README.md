# gateway

This application sits between applications that you want to limit access to. It checks authorization validity, and sends information about the user downstream to the real application. It acts as a reverse proxy.

## Routing

Any routes (e.g., serving static files) that are specific to the gateway are under `/__ident_gateway_service__` to avoid conflict with downstream routes - it is unlikely that this route is used 
by other applications.

## Strategies

Strategies define how the authorization value is determined, for example:
- Through cookies (`CookieStrategy`)
- Through headers (`HeaderStrategy`)
- Any other class that implements `BaseStrategy`



## Authenticator

Authenticators handle checking with ident that access is allowed. They associate a host to an application, and execute policies to test whether users can access the application or not. The following are (/will be) implemented:
- `HttpAuthorizer`: An authorizer that uses ident's REST API to authorize and authenticate you. (currently uses non-existent routes)
- `FDBAuthorizer`: An authorizer that directly uses the foundationdb database that the ident API, calculating rules basd on teh data stored within it. 

## Downstream Applications

The incoming requests remain ideally unmodified, apart from the following headers:
- `X-Ident-Current-User`: The current user, base64 encoded
- `X-Ident-Current-Timestamp`: The current timestamp, in unix millis
- `X-Ident-Ed25519-Signature`: Explained below

### Signing

Although we do our best to make sure the `X-Ident-Current-User` is not modified, we also include `X-Ident-Ed25519-Signature`, which is a hex encoded signature of the current user and timestamp values combined, split by a comma. See the example below for more detail:

```py
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

PUBLIC_KEY = 'the public key from the application, in hex'

verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

user = request.headers["x-ident-current-user"]
signature = request.headers["x-ident-ed25519-signature"]
timestamp = request.headers["x-ident-current-timestamp"]


try:
    verify_key.verify(f'{timestamp}:{user}'.encode(), bytes.fromhex(signature))
except BadSignatureError:
    # don't allow the request ...
```

This way, you can be sure that Ident has issued this data, and that it isn't being spoofed by someone else (assuming that the gateway is non-compromised).