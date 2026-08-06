from langchain_chroma import Chroma
import hashlib
from models.Model import get_embedding_model
from documentation_assistant.config import DATA_DIR


def get_vector_store(url_id):
    name = hashlib.md5(url_id.encode()).hexdigest()
    
    vector_store = Chroma(
        embedding_function=get_embedding_model(),
        persist_directory=DATA_DIR,
        collection_name=name
    )
    return vector_store