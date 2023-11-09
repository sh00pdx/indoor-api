from .app_error import AppError

class UnauthorizedError(AppError):
    def __init__(self, message):
        self.message = message
        
    def serialize_errors(self):
        return {"error": "Unauthorized", "message": self.message, "status_code": 401}