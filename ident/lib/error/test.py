from .base import BaseError

class TestModeOnlyError(BaseError):
    code = "disallowed_in_production"
    message = "This action is only permitted in non-production environments"
    help = "Are you in a non-production environment? Make sure your application config is correct"
    http_status = 403