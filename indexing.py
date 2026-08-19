""" delete webpage(s) data from database"""


from documentation_assistant.file_indexing import stage_database
from documentation_assistant.config import DATA_DIR
import chromadb

cursor = stage_database()
def data_lookup():
    
    cursor.execute(
        '''
        SELECT * FROM lookup;
        '''    
    )
    result = cursor.fetchall()
    if not result:
        print("Database is empty bruh!")
        return False
    
    print("\nSaved data:\n")
    for r in result:
        print(r)
    return True

def delete_data():
    dec = data_lookup()
    if not dec:
        return
    else :
        while True:
            try:
                index = int(input("\nSelect the serial.no to delete the url data!\n"))
                break
            except ValueError:
                print("Enter a valid input")

        cursor.execute(
            '''
            SELECT hash_id ,url FROM lookup
            WHERE   uid =?
            ''',(index,)
            
        )
        
        result = cursor.fetchone()
        if  result:
            hashed, url = result
            try:
                client = chromadb.PersistentClient(DATA_DIR)
                client.delete_collection(hashed)
                print("Data deleted for url: ",url)
            except Exception as e :
                print("Unable to delete",e)
                return
            cursor.execute(
                        '''
                        DELETE FROM lookup
                        WHERE   uid =?
                        ''',(index,)
                        
                    )
            cursor.connection.commit()
        else :
            print("Didn't match any valid index")

if __name__=='__main__':
    delete_data()
    cursor.connection.close()