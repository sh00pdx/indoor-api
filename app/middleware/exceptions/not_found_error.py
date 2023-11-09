from .app_error import AppError

class NotFoundError(AppError):
    def __init__(self, message):
        self.message = message
        
    def serialize_errors(self):
        return {"error": "Not Found", "message": self.message, "status_code": 404}