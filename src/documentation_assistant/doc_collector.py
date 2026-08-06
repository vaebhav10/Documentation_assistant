from langchain_core.documents import Document


def collect_docs(results):
    all_docs = []

    for r in results:
    
        if not r.success:
            continue
        
        docs = Document(
            page_content=r.markdown,
            metadata ={
                'url': r.url,
                'title':r.metadata['title']
            }
        )
        
        all_docs.append(docs)
        
    return all_docs

def get_hyperlinks(results):
    HYPERLINKS= []
    for r in results:
        if not r.success:
            continue
        
        hyperlinks = [links['href'] for links in r.links['internal']]
        
        HYPERLINKS.extend(hyperlinks)
    
    return HYPERLINKS
        