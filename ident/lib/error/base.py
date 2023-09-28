from flask import jsonify, request

class BaseError(Exception):
    code: str
    message: str
    help: str = "(no further help)"

    http_status: int

    def to_dict(self):
        return {
            "error": {
                "code": self.code,
                "message": self.get_message()
            }
        }

    @staticmethod
    def include_error_help() -> bool:
        return "x-include-error-help" in request.headers and request.headers['x-include-error-help'] == "1"


    def get_message(self):
        if not self.include_error_help():
            return self.message
        
        return f'{self.message}; {self.help}'
    
    @staticmethod
    def handle(exc: 'BaseError'):
        return jsonify(exc.to_dict()), exc.http_status