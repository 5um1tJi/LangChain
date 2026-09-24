from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    r"C:\Users\sumit mishra\OneDrive\Desktop\LangGraph\LangGraph\LangChain\Text_Splitting\ChessEssay.pdf"
)
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

# res = splitter.split_text(text) it is for text splitting
res = splitter.split_documents(docs)

print(res[0].page_content)