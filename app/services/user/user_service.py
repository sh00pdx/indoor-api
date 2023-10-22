from .user_service_deps import user_service_deps
from app.logger import get_logger

logger = get_logger(__name__)

class UserService:
    deps = None
     
    def __init__(self, deps) -> None:
        self.deps = deps
        self.logger = logger
        
    
    
    async def register(self, body):
        # TODO: registrar usuario
        pass

    async def update(self, body):
        # TODO: registrar usuario
        pass
    
    
UserServiceSingleton = UserService(user_service_deps)
