from documentation_assistant.crawler import crawl_page
from documentation_assistant.doc_collector import collect_docs,get_hyperlinks
from collections import deque


async def get_documents_bfs(target_urls, s_exists:bool):    
    DOCUMENTS = []
    
    visited_url = set()
    queue = deque()

    if s_exists:
        queue.extend(target_urls)
    else:
        queue.append(target_urls)
    
    batch_size = 10
    
    while queue:
        
        batch = []
        
        while queue and len(batch) < batch_size:
            
            url = queue.popleft()
            if url in visited_url:
                continue
            
            batch.append(url)
            visited_url.add(url)
        
        results = await crawl_page(batch,True)  
        
        collected_docs = collect_docs(results)
        DOCUMENTS.extend(collected_docs)
        
        if not s_exists:
            hyperlinks = get_hyperlinks(results)
            
            for link in hyperlinks:
                if link not in visited_url:
                    queue.append(link)

    return DOCUMENTS
