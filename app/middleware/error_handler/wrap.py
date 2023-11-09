from fastapi.responses import JSONResponse
from functools import wraps
import inspect

def error_handler_decorator(callback=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # Llamar a la función original
                result = await func(*args, **kwargs)
                # Todo salió bien, devolver una respuesta JSON con código 200
                return JSONResponse(content={"data": result}, status_code=200)
            except Exception as e:
                # Algo salió mal, ejecutar el callback y levantar la excepción
                if callback:
                    # Comprobar si el callback es síncrono o asíncrono
                    if inspect.iscoroutinefunction(callback):
                        await callback(e, *args, **kwargs)
                    else:
                        callback(e, *args, **kwargs)
                raise e
        return wrapper
    return decorator


def error_handler_decorator_plain_response(callback=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # Llamar a la función original
                result = await func(*args, **kwargs)
                # Todo salió bien, devolver una respuesta JSON con código 200
                return result
            except Exception as e:
                # Algo salió mal, ejecutar el callback y levantar la excepción
                if callback:
                    # Comprobar si el callback es síncrono o asíncrono
                    if inspect.iscoroutinefunction(callback):
                        await callback(e, *args, **kwargs)
                    else:
                        callback(e, *args, **kwargs)
                raise e
        return wrapper
    return decorator
