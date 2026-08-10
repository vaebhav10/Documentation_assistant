# Overview

This is a Retrieval-Augmented Generation (RAG) based project system for documentation assistance, where you can get your qeury-answer related to a documentation website.  
  # How it works ? 
  
User--> pastes documentation link:  
    gets the hashid of the link :
    if cached collection exists in the database --> returns retriever.  

    In case of documents for the pasted link ONLY
        Crawls the page--> gets the markdown(along with the metadata) --> stores it in Chroma  
        returns the retriever.

    For ALL the documents related to the pasted link
    if sitemap exists :  
        USP --> fetches all the hyperlinks at once --> crawller fetches the markdowns for those pages.
    else :
        crawller fetches the hyperlinks from the perticular page, puts it in the queue -->  gets the page data using bfs.

    Extraced page data + markdown --> Split documents into chunks --> generate embeddings --> store in the Database --> returns the retriever.

    user asks the query --> similarity search --> relevant chunks --> LLM --> Answer



## How to run?

*  **Prerequisites**

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management. If ! installed (U+1F642):

* for Linux/macOs
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

###  Bug/Suggestions:

Found a bug or have a suggestion? Feel free to open an issue or send an email.