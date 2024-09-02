from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from controllers import scraping
from utils.log import get_logger, clone_log_config
import logging


from controllers import scraping

origins = ["*"]
methods = ["*"]
headers = ["*"]

logger = get_logger(__file__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    server_logger = logging.getLogger("uvicorn")
    clone_log_config(logger, server_logger)
    server_logger = logging.getLogger("uvicorn.access")
    clone_log_config(logger, server_logger)
    server_logger = logging.getLogger("uvicorn.error")
    clone_log_config(logger, server_logger)
    app_logger = logging.getLogger("app_log")
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(scraping.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_headers=headers,
    allow_credentials=True,
)