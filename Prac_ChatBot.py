from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    include_reasoning=False
)

hist = [
    SystemMessage(content = "you are my asistant")
]
while True:
    user_in = input("you :" )

    if(user_in=="exit"):
        break

    hist.append(HumanMessage(content=user_in))
    out = llm.invoke(hist)
    hist.append(AIMessage(content=out.content))
    print("AI :", out.content)

print(hist)

