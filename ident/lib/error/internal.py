from flask import jsonify, current_app, abort
from werkzeug.exceptions import HTTPException, InternalServerError


def handle_unknown_exception(ex: Exception):
    # re-raise if we are in debug mode to
    # provide better exceptions in development
    if current_app.debug:
        raise ex

    return handle_http_exception(InternalServerError())

def handle_http_exception(ex: HTTPException):
    return jsonify({
        "error": {
            "code": ex.name.lower().replace(" ", "_"),
            "message": ex.name
        }
    }), ex.code