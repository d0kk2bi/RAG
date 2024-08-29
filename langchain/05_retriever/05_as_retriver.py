from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

texts = ["My name = John Doe"]
query = "Who are you?"

embed = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma.from_texts(
    texts,
    embed,
    collection_name="history",
    persist_directory="./db/",
    collection_metadata={"hnsw:space": "cosine"},
)

# https://api.python.langchain.com/en/latest/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html#langchain_chroma.vectorstores.Chroma.as_retriever
retriever = db.as_retriever(search_kwargs={"k": 1})
docs = retriever.invoke(query)

print(docs[0].page_content)
