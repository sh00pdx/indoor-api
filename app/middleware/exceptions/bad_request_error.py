from .app_error import AppError

class BadRequestError(AppError):
    def __init__(self, message):
        self.message = message
        
    def serialize_errors(self):
        return {"error": "Bad Request", "message": self.message, "status_code": 400}