
from ident.lib.response import define, union

@define
class LoginResultComplete:
    token: str

@define
class LoginResultMust2FA:
    context_id: str

LoginResult = LoginResultComplete | LoginResultMust2FA

union(
    LoginResult, 
    tag='next',
    mapping={
        None: LoginResultComplete,
        '2fa': LoginResultMust2FA
    }
)