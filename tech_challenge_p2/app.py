from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import scraping



from controllers import scraping

origins = ["*"]
methods = ["*"]
headers = ["*"]

app = FastAPI()

app.include_router(scraping.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_headers=headers,
    allow_credentials=True,
)