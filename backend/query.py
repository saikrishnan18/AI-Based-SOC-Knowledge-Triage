from llama_index.core import load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from llama_index.llms.huggingface import HuggingFaceLLM

# Load storage
storage_context = StorageContext.from_defaults(persist_dir="../embeddings")

# Load index
index = load_index_from_storage(storage_context)

# Load LLM (offline HuggingFace model)
llm = HuggingFaceLLM(
    model_name="tiiuae/falcon-7b-instruct",  # you can change to lighter model
    tokenizer_name="tiiuae/falcon-7b-instruct",
    device_map="auto"
)

# Create query engine
query_engine = index.as_query_engine(llm=llm)

def ask_question(query):
    response = query_engine.query(query)
    return str(response)
