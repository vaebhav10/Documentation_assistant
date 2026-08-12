from langchain_core.prompts import PromptTemplate

def get_prompt():
    prompt = PromptTemplate(
        template="""
        You have been assigned a task to explain the user's query based on the documents provided. 
        
        Answer the query based on the provided documents ONLY.
        Explain the query's answer clearly, to the point and AVOID using outside knowledge.
        
        Context : \n{chunks}\n
        
        The user_query is : \n
        {query}
        """,
        input_variables=['chunks','query']
    )
    
    return prompt