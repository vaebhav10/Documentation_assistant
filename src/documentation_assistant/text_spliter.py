from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

headers_to_split_on = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
    ("####", "h4")
]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1519,
    chunk_overlap=295
)

def split_text(documents):

    all_chunks = []
    for doc in documents:
        mk_splitted= markdown_splitter.split_text(doc.page_content)
        for splitted in mk_splitted:
            splitted.metadata.update(doc.metadata)
        rk_splitted = recursive_splitter.split_documents(mk_splitted)
        all_chunks.extend(rk_splitted)

    return all_chunks