from .base import BaseError

class UnknownActionLogEntry(BaseError):
    message = "Unknown Action Log"
    code = "unknown_action_log"
    http_status = 404