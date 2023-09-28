from .base import BaseError

class UnknownUser(BaseError):
    message = "Unknown User"
    code = "unknown_user"
    http_status = 404

class EmailAlreadyExists(BaseError):
    message = "Email already exists"
    code = "email_already_exists"
    http_status = 409