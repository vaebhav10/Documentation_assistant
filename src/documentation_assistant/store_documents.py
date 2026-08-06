from tqdm import tqdm

def add_documents(splitted_chunks, vector_store):
        
    batch_size = 101
    size = len(splitted_chunks)
    print("\nAdding website data to database.....\n")
    for i in tqdm(range(0, size, batch_size)):
        batch = splitted_chunks[i:i+batch_size]
        vector_store.add_documents(batch)
    
    # print("im working here555 ")
    return 
