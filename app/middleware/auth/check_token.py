from fastapi import Request, HTTPException
from .deps import check_token_deps
from app.models import User
from app.config import TOKEN
from fastapi.responses import JSONResponse

#from app.services.auth.auth_service import AuthService

class CheckTokenMiddleware ():
    #deps: check_token_deps
    PROTECTED_ROUTE_PREFIXES = [
        '/equipment',
        # Añade más prefijos según sea necesario
    ]
    
    EXCLUDE_PROTECTED_ROUTES = [
        '/equipment/medition',
    ]
    
    def __init__ (self, deps_):
        self.deps = deps_
    
    async def __call__(self, request: Request, call_next):
        #authService: AuthService = self.deps[services']['AuthService']
        if any(request.url.path.startswith(prefix) for prefix in self.PROTECTED_ROUTE_PREFIXES):
            
            if request.url.path not in self.EXCLUDE_PROTECTED_ROUTES:
                
                token = request.headers.get('Authorization')

                if token != TOKEN:
                    return JSONResponse({"error": "Unauthorized", "message": "", "status_code": 401})
            
                
            """ await self.set_body(request)
            await request.body()  # Consumir completamente el flujo de la solicitud
            
            body = await request.json()
            token = body.get("token")
            
            if token is None:
                raise HTTPException(status_code=400, detail="Token missing")
             """
            user = User.get(User.id == 1)   
            request.state.user = user

        response = await call_next(request)
        return response
    
    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive
    
CheckTokenMiddlewareSingleton = CheckTokenMiddleware(check_token_deps)