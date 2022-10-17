from pydantic import BaseModel


class book_of_references(BaseModel):
    title: str
    descrip: str

