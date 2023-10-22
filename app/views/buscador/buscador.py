from .buscador_deps import buscador_deps
from autofact_lib_python_error_handler import *
from autofact_lib_python_error_handler import error_handler_decorator_plain_response
from app.logger import get_logger 
from app.helpers.callback.callback import callback_singleton

logger = get_logger(__name__)
    
class BuscadorView:
    deps: buscador_deps

    def __init__(self, deps: buscador_deps):
        self.deps = deps
        self.logger = logger
        
    @error_handler_decorator_plain_response(callback=callback_singleton.callback_dispatch)
    async def dispatch(self, data):
        return await self.deps['services']['BuscadorServiceSingleton'].dispatch(data)
    
    
BuscadorViewSingleton = BuscadorView(buscador_deps)
