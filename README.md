# Overview

This is a Retrieval-Augmented Generation (RAG)-based system for documentation assistance, where you can get answers to queries related to a documentation website.

# How it works?

User --> pastes documentation link:  
    gets the hash ID of the link:  
    if a cached collection exists in the database --> returns the retriever.  

    In case of documents for the pasted link **ONLY**:  
        Crawler crawls the page --> gets the Markdown (along with the metadata) --> stores it in Chroma  
        returns the retriever.  

    For **ALL** the documents related to the pasted link:   
    if a sitemap exists:  
        USP --> discovers all the URLs from the sitemap --> crawler fetches the Markdown for those pages.  
    else:  
        Crawler fetches the hyperlinks from the particular page, puts them in the queue --> gets the page data using BFS.  

    Extracted page data + Markdown --> split documents into chunks --> generate embeddings --> store in the database --> return the retriever.  

    User asks the query --> similarity search --> relevant chunks --> LLM --> Answer  

## Limitations:
Since the website data extraction is done with crawl4Ai which is more suited for **static/text** heavy sites, which it may not be reliable in case of heavily JavaScript-rendered or similar websites.   


## How to run?  

* **Prerequisites**  

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management. If it is not installed:  

* For Linux/macOS:  

```bash  
curl -LsSf https://astral.sh/uv/install.sh | sh  
```  

(For Windows, see the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/).)  

---  

Clone the repo using HTTPS:  

```bash   
git clone https://github.com/vaebhav10/Documentation_assistant.git  
```  

Or using GitHub CLI:  

```bash  
gh repo clone vaebhav10/Documentation_assistant  
```  

Then:  

```bash  
cd Documentation_assistant  
uv sync  
uv run python main.py  
```  

### Bugs / Suggestions:  

Found a bug or have a suggestion? Feel free to open an issue.  
