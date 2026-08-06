""" 
A HIGH LEVEL PROJECT OVERVIEW

input --> url 

check existance 
if exists :
    load the retriever 
else :
    get entire documention?
    1 -->> yes 
    0 --> No 
    
    get hashid for indexing in chroma
    
    if getall :
        parse the url --> get the homepage
        homepage --> sitemap--> get all links 
        crawl all links 
        collect all the data 
    if 0 : --> single url
        crawl the link 
        get the result
    store the markdown in chroma using nameId as indexing 
"""