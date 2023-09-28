from flask import Flask
from werkzeug.exceptions import HTTPException

from ident.apis import (
    acls, 
    applications, 
    action_logs, 
    groups, 
    meta,
    networks,
    sessions, 
    users, 
    webhooks
)

from ident.lib.error import BaseError, handle_unknown_exception, handle_http_exception
from ident.lib.validation import ValidationException

app = Flask(__name__, static_folder=None)

# return consistent ordering according to model definition(s)
app.json.sort_keys = False 

# controllers
app.register_blueprint(acls)
app.register_blueprint(applications)
app.register_blueprint(action_logs)
app.register_blueprint(groups)
app.register_blueprint(meta)
app.register_blueprint(networks)
app.register_blueprint(sessions)
app.register_blueprint(users)
app.register_blueprint(webhooks)
# end controllers

# error handlers
app.register_error_handler(BaseError, BaseError.handle)
app.register_error_handler(ValidationException, ValidationException.handle)
app.register_error_handler(HTTPException, handle_http_exception)
app.register_error_handler(Exception, handle_unknown_exception)
# end error handlers

# development
if __name__ == "__main__":
    app.run(
        port=8080,
        debug=True
    )