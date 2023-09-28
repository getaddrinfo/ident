from typing import Literal
from enum import StrEnum

from ident.lib.validation import Strict

class LoginBody(Strict):
    password: str
    username: str | None
    email: str | None = None
        
class MfaType(StrEnum):
    TOTP = 'totp'

class MfaBase(Strict):
    type: MfaType
    context_id: str

class MfaTotp(MfaBase):
    type: Literal[MfaType.TOTP]

Mfa = MfaTotp