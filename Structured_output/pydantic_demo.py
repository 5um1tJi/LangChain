from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class student(BaseModel):
    name: str
    # default value
    age: int = 22
    # optional 
    height : Optional[int] = None
    # "type coercing" me python khud uska datatype correct kar deta hai, agr galat kiya user ne to
    email : EmailStr  ## will throw error if not written like gmail.com
    cgpa : float = Field(gt=0, lt=10)   # it gives the constraints like greater than, less than 

new = {"name": "sumit"}

stud = student(**new)
print(stud)