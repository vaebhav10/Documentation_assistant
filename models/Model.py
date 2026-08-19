from langchain_ollama import OllamaEmbeddings,ChatOllama
from langchain_huggingface import  (
    ChatHuggingFace,
    HuggingFaceEndpoint,
    HuggingFaceEmbeddings
)
from dotenv import load_dotenv
load_dotenv()

""" local inference via Ollama
    U+1F643
"""

def get_embedding_model():
    Qwen = OllamaEmbeddings(
        model='qwen3-embedding:0.6b'
    )
    return Qwen

def get_llm():
    Qwen = ChatOllama(
        model='qwen3:8b',
        temperature=0.3
    )
    return Qwen


# def get_embedding_model():
#     embedding_model= HuggingFaceEmbeddings(
#     model_name = 'sentence-transformers/all-MiniLM-L6-v2',
#     model_kwargs={"device": "cuda"} 
#     )
#     return embedding_model


# def get_llm():
#     llm = HuggingFaceEndpoint(
#     repo_id = 'meta-llama/Llama-3.1-8B-Instruct',
#     task = 'text-generation',
#     temperature=0.4
#     )
#     model =ChatHuggingFace(llm=llm)
    
#     return model 
