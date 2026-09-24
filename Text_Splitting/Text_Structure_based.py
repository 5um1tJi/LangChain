from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# in this the function Recursive tries to split first on the baisi of paragraph \n\n and then line \n and then words - and then characters

loader = PyPDFLoader(r"C:\Users\sumit mishra\OneDrive\Desktop\LangGraph\LangGraph\LangChain\Text_Splitting\ChessEssay.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(

    chunk_size = 300,

    chunk_overlap = 0
)

res = splitter.split_documents(docs)

print(len(res))

print(res[0].page_content)

