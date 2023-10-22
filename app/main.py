from fastapi import FastAPI
from app.urls import main, ping
from autofact_lib_python_error_handler import error_middleware
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
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


app.include_router(main.router)
app.include_router(ping.router)

app.middleware("http")(error_middleware)

if(os.getenv('ENV', 'local') != 'local'):
    handler = Mangum(app)
    