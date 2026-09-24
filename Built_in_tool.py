from langchain_community.tools import DuckDuckGoSearchRun

tool = DuckDuckGoSearchRun()
res = tool.invoke("who is the current chess number one")
print(res)