from pydantic import ValidationError as PydanticValidationError
from .exception import ValidationError

from dataclasses import dataclass
from flask import jsonify

class ValidationException(Exception):
    errors: list['ValidationFailure']

    def __init__(self, errors: list['ValidationFailure']):
        self.errors = errors
        
    @staticmethod
    def handle(ex: 'ValidationException'):
        return handle_validation_exception(ex)

@dataclass
class ValidationFailure:
    failure: ValidationError
    path: tuple[str, ...]

def transform(
    error: PydanticValidationError
):
    all = error.errors()

    parsed = []

    for error in all:
        transformed = ValidationError.lookup(error.get("type"))(error.get("ctx", dict()))

        parsed.append(ValidationFailure(
            transformed,
            error.get("loc")
        ))

    return parsed

def handle_validation_exception(
    ex: ValidationException
):
    return jsonify({
        "error": {
            "code": "validation_failed",
            "message": "Validation Failed",
            "context": {
                "errors": [{
                    "for": ".".join(error.path),
                    "code": error.failure.code,
                    "message": error.failure.message
                } for error in ex.errors]
            }
        }
    }), 400