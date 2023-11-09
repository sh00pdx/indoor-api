from .app_error import AppError

class ForbiddenError(AppError):
    def __init__(self, message):
        self.message = message
        
    def serialize_errors(self):
        return {"error": "Forbidden", "message": self.message, "status_code": 403}