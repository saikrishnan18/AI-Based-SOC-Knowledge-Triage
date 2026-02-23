from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.faiss import FaissVectorStore
import faiss

# Load documents
documents = SimpleDirectoryReader("../data").load_data()

# Embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS index
dimension = 384
faiss_index = faiss.IndexFlatL2(dimension)

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create index
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=embed_model
)

# Save embeddings
index.storage_context.persist(persist_dir="../embeddings")

print("Ingestion complete. Embeddings stored.")
