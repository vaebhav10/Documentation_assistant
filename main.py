import asyncio
from documentation_assistant.connect_script import execute_pipeline
from langchain_core.output_parsers import StrOutputParser
from documentation_assistant.prompt_template import get_prompt
from models.Model import get_llm
from documentation_assistant.url_indexing import get_valid_input 

async def main():
    model= get_llm()
    parser = StrOutputParser()
    prompt = get_prompt()

    """ Input part"""
    url = input ("Paste your url :\n")
    
    retrieve_all = get_valid_input()
    
    ## if false--> single 
    retriever =await execute_pipeline(url,retrieve_all)
    chain = prompt|model|parser

    while True:
        user_query = input("\nEnter your query: \n")
        
        if user_query.lower() in ['exit','quit']:
            break
        
        context_docs= retriever.invoke(user_query)
        query_ans = '\n\n'.join(doc.page_content for doc in context_docs)
        
        result = chain.invoke({'chunks':query_ans,'query':user_query})
        
        # print(query_ans)  # <-- for debug 
        print('\n', '-'*101,'\n')
        print(result)        
        print('\n', '-'*101,'\n')

if __name__=='__main__':
    asyncio.run(main())