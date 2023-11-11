from fastapi import FastAPI
from app.urls import ping, equipment
from app.middleware.error_handler import error_middleware
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.middleware.auth import CheckTokenMiddlewareSingleton
import os

load_dotenv()

app = FastAPI(
    docs_url=os.getenv('PATH_DOCS'),
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.middleware("http")(CheckTokenMiddlewareSingleton)

app.include_router(equipment.router)
app.include_router(ping.router)

app.middleware("http")(error_middleware)

if(os.getenv('ENV', 'local') != 'local'):
    handler = Mangum(app)
    