from pydantic import BaseModel

class ScrapingResponseModel(BaseModel):
    message: str
    filename: str
    file_date: str