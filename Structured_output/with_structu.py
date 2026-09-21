from typing import TypedDict, Annotated, Optional, Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
)
class review(TypedDict):
    name: Annotated[str, "name of the fighter"]
    height: Annotated[int, "height of the fighter"]
    country: Annotated[str, "the country he belongs to"]
    champion: Annotated[Optional[str], "write male if he is a male, or female if she is a female"]
    company: Annotated[Literal["ufc", "pfl", "wwe"], "the company he fights in"]

struc_mod = llm.with_structured_output(review, method="json_schema")

ans = struc_mod.invoke("tell me about roman reigns , also give the height and his country of nationality, give the output in json format")
print(ans["height"])
print(ans["country"])
print(ans["name"])
print(ans["champion"])
print(ans["company"])