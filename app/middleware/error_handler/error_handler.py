from fastapi import  Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from ..exceptions.app_error import AppError
from ..logger import get_logger
import traceback

logger = get_logger('error_handler')

async def error_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except RequestValidationError as e:
        logger.error(f'{e.errors()}')
        return JSONResponse({"error": "Bad request", "message": e.errors(), "status_code": 400}, status_code=400)
    except AppError as e:
        logger.error(f'{e.serialize_errors()}')
        return JSONResponse(e.serialize_errors(), status_code=e.serialize_errors()["status_code"])
    except Exception as e:
        logger.error(f'{traceback.format_exc()}')
        return JSONResponse({"error": 'Internal server error', "message": str(e), "status_code": 500}, status_code=500)
