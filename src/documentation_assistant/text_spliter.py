from langchain_classic.text_splitter import RecursiveCharacterTextSplitter


def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=198, 
    )
    splitted_docs = splitter.split_documents(documents)
    
    return splitted_docs