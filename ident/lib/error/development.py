from .base import BaseError

class NotImplementedError(BaseError):
    code = "not_implemented"
    message = "Not Implemented"
    http_status = 418 # is there a real status code for this?
    help = "This currently isn't implemented. Maybe check the documentation?"