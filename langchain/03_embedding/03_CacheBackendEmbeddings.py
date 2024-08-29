from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_openai import OpenAIEmbeddings

# https://api.python.langchain.com/en/latest/langchain/storage/langchain.storage.file_system.LocalFileStore.html#localfilestore
# Base Storage class for local file system storage
cache_dir = LocalFileStore("./.cache/")

texts = [
    "Hello World' is my favorite sentence!",
    "'Bye World' is my favorite sentence!",
]

embed = OpenAIEmbeddings(model="text-embedding-3-large")

# https://api.python.langchain.com/en/latest/langchain/embeddings/langchain.embeddings.cache.CacheBackedEmbeddings.html#cachebackedembeddings
cached_embed = CacheBackedEmbeddings.from_bytes_store(embed, cache_dir)

# Embed Single Text
vector = cached_embed.embed_query(texts[0])
print("vector:", vector[:3])

# Embed Multiple Texts
vectors = cached_embed.embed_documents(texts)
print("vector:", vectors[1][:3])
