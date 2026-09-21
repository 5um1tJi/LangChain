from langchain_groq import ChatGroq
from typing import TypedDict

class person(TypedDict):
    name : str
    age : int

new : person = {"name": "sumit", "age": 23}
print(new)