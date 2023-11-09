from abc import ABC, abstractmethod

class AppError(ABC, Exception):
    @abstractmethod
    def serialize_errors(self):
        pass