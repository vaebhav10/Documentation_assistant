from tqdm import tqdm
from urllib.parse import urlparse
from documentation_assistant.extract_documents import get_documents_bfs
from documentation_assistant.doc_collector import collect_docs
from documentation_assistant.text_spliter import split_text
from documentation_assistant.vector_store import get_vector_store
from documentation_assistant.url_indexing import check_existence
from documentation_assistant.sitemap import get_sitemap
from documentation_assistant.crawler import crawl_page
from documentation_assistant.file_indexing import write_url
        
async def execute_pipeline(query_url,retrieve_all):
    
    parsed = urlparse(query_url)
    home_url= f'{parsed.scheme}://{parsed.netloc}/'
    
    if retrieve_all:
        
        if check_existence(home_url):
            print("\nPreloaded data used!\n")
            vs =  get_vector_store(home_url)
            
            return vs.as_retriever()
        
        
        all_links = get_sitemap(home_url)

        sitemap_exists = False
        if all_links:
            sitemap_exists = True
            docs = await get_documents_bfs(all_links,sitemap_exists)
            
        else :
            docs = await get_documents_bfs(home_url,sitemap_exists)
            
        
    else :
        if check_existence(query_url):
            print("\nPreloaded data used!\n")
            vs =  get_vector_store(query_url)
            
            return vs.as_retriever()
        
        result = await crawl_page(query_url,retrieve_all)
        docs = collect_docs(result)
    

    splitted_chunks = split_text(docs)
    if retrieve_all:
        URL = home_url
        vs = get_vector_store(home_url)
    else :
        URL = query_url
        vs = get_vector_store(query_url)
        
    batch_size = 101
    size = len(splitted_chunks)
    print("\nAdding website data to database.....\n")
    for i in tqdm(range(0, size, batch_size)):
        batch = splitted_chunks[i:i+batch_size]
        vs.add_documents(batch)
    
    # write url in databse 
    write_url (URL, retrieve_all)
    
    retriever = vs.as_retriever()
    return retriever
