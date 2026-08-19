import sqlite3
from hashlib import md5
from documentation_assistant.config import DATA_DIR

def stage_database():
    connection = sqlite3.Connection(DATA_DIR/'LookupDatabase.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS lookup(
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            hash_id TEXT UNIQUE NOT NULL,
            url TEXT,
            retrieve_type TEXT
        )
        '''
    )
    
    
    return cursor
    

def write_url(url,retrieve_type):
    if retrieve_type:
        ret = 'ALL PAGE'
    else :
        ret = 'SINGLE PAGE'
    cursor= stage_database()
    
    hashed = md5(url.encode()).hexdigest()
    cursor.execute(
        '''
        INSERT INTO lookup(hash_id, url,retrieve_type) values(?,?,?)
        ''',(hashed,url,ret)
    )
    cursor.connection.commit()
    cursor.connection.close()