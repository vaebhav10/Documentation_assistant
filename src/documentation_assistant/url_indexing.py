import hashlib
import chromadb
from documentation_assistant.config import DATA_DIR

def get_name(url):
    name = hashlib.md5(url.encode()).hexdigest()
    return name
    
def get_valid_input()->bool:
    valid_inputs = [0,1]
    print("Get Entire Documentation? \nInput 1 for 'yes'\nInput 0 for 'No'\n")
    while True:
        
        ans = int(input())
        
        if ans not in valid_inputs:
            print("Invalid input!.\nEnter either 0 or 1.")
        else:
            if ans ==1:
                return True
            else :
                return False
    


def check_existence(url):
    name = get_name(url)
    connection  = chromadb.PersistentClient(DATA_DIR)
    
    return any(c.name == name for c in connection.list_collections())
