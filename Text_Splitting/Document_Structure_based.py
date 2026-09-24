
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

#  it is used for any document structured, it used for different rule or pattern based splitting

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,

    chunk_size = 100,

    chunk_overlap = 0
)

text = """
    def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def subtract(self, a, b):
        return a - b
"""
res = splitter.split_text(text)

print(res[0])
