from typing import TypedDict, Annotated, Optional, Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv(override=True)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
)
class review(BaseModel):

    name: str = Field(description = "the name of the fighter")
    height: float = Field(description = "The hieght of the given person")
    country: str = Field(description = "the country he belongs to")
    company: Literal["ufc", "wwe", "pfl", "awe"] = Field(default=None , description = "the company he fights in from wwe or ufc or pfl or awe")

struc_mod = llm.with_structured_output(review)

ans = struc_mod.invoke("tell me about Conor Mcgregor , also give the height and his country of nationality")
print(ans)
