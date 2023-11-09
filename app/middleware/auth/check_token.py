from fastapi import Request, HTTPException
from .deps import check_token_deps
from app.services.auth.auth_service import AuthService

class CheckTokenMiddleware ():
    deps: check_token_deps
    ALLOW_ROUTES = [
        '/segments/answer',
        '/segments/favorite',
        '/segments/deleted',
        '/auth/signup',
        '/segments/getFavorites',
        '/tracking',
    ]
    
    def __init__ (self, deps_):
        self.deps = deps_
    
    async def __call__(self, request: Request, call_next):
        authService: AuthService = self.deps['services']['AuthService']
        if request.url.path in self.ALLOW_ROUTES:
            await self.set_body(request)
            await request.body()  # Consumir completamente el flujo de la solicitud
            
            body = await request.json()
            token = body.get("token")
            
            if token is None:
                raise HTTPException(status_code=400, detail="Token missing")
            
            user = await authService.validate_or_register_token(token)    
            request.state.user = user

        response = await call_next(request)
        return response
    
    async def set_body(self, request: Request):
        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive
    
CheckTokenMiddlewareSingleton = CheckTokenMiddleware(check_token_deps)