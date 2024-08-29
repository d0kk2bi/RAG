from langchain.storage import LocalFileStore
from langchain_openai import CacheBackedEmbeddings, OpenAIEmbeddings

# https://api.python.langchain.com/en/latest/langchain/storage/langchain.storage.file_system.LocalFileStore.html#localfilestore
# Base Storage class for local file system storage
cache_dir = LocalFileStore("./.cache/")

texts = [
    "Hello World' is my favorite sentence!",
    "'Bye World' is my favorite sentence!",
]

# https://api.python.langchain.com/en/latest/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html#openaiembeddings
embed = OpenAIEmbeddings(model="text-embedding-3-large")


# cache_embed = CacheBackedEmbeddings

# Embed Single Text
vector = embed.embed_query(texts[0])
print("vector:", vector[:3])

# Embed Multiple Texts
vectors = embed.embed_documents(texts)
print("vector:", vectors[1][:3])
