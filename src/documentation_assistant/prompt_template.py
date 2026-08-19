from langchain_core.prompts import PromptTemplate

def get_prompt():
    prompt = PromptTemplate(
        template="""
        You have been assigned a task to explain the user's query based on the documents chunk provided. 
        
        Follow these rules STRICTLY:
        - If the provided chunks lack enough context to explain the query. Explain why you cant answer the query based on the chunks provided.
        -DON'T use your knowledge to explain the query, even if you can.
        
        -If the chunks have enough context for the query to be explainable,
        Answer the query based on the provided documents ONLY.
        Explain the query's answer clearly, to the point and AVOID using outside knowledge.
        
        Context : \n{chunks}\n
        
        Query : \n{query}\n
        """,
        input_variables=['chunks','query']
    )
    
    return prompt
