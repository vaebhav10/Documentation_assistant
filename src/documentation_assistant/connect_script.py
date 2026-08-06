from urllib.parse import urlparse
from documentation_assistant.extract_documents import get_documents_bfs
from documentation_assistant.doc_collector import collect_docs
from documentation_assistant.text_spliter import split_text
from documentation_assistant.store_documents import add_documents
from documentation_assistant.vector_store import get_vector_store
from documentation_assistant.url_indexing import check_existence
from documentation_assistant.sitemap import get_sitemap
from documentation_assistant.crawler import crawl_page
        
async def execute_pipeline(query_url,retrieve_all):
    
    """ If already present return retriever """
    if check_existence(query_url):
        print("\nPreload data used!\n")
        vs =  get_vector_store(query_url)
        
        return vs.as_retriever()
    
    """ For the entire documentation """
    parsed = urlparse(query_url)
    home_url= f'{parsed.scheme}://{parsed.netloc}/'
    if retrieve_all:
        
        """crawl entire hyperlinks
        If sitemap exists --> get all the links """
        all_links = get_sitemap(home_url)

        sitemap_exists = False
        if all_links:# <-- links from sitemap
            sitemap_exists = True
            docs = await get_documents_bfs(all_links,sitemap_exists)
            
        else :# JIC of sitemap absence (unusual scenario though)
            docs = await get_documents_bfs(home_url,sitemap_exists)
            
    ## For documents of the url page ONLY
    else :
        result = await crawl_page(query_url,retrieve_all)
        docs = collect_docs(result)
    

    splitted_chunks = split_text(docs)
    """ Indexing based on query_url"""
    if retrieve_all: # <-- Using homepage as the index
        vs = get_vector_store(home_url)
    else :# query_url
        vs = get_vector_store(query_url)
        
    add_documents(splitted_chunks,vs)
    
    retriever = vs.as_retriever()
    return retriever
