from pydantic import BaseModel # type: ignore

class Person(BaseModel):
    name: str
    age: int
    email: str

