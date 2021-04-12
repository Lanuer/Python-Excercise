from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb+srv://lanuer:zaq123456@realmcluster.6fpkj.mongodb.net/lanuer_mongo?retryWrites=true&w=majority')

db_Name = 'test-database'
db = client[db_Name]

col_Name = 'test-collection'
col = db[col_Name]

def connect():
    dblist = client.list_database_names()
    if db_Name in dblist:
        collist = db.list_collection_names()
        if col_Name in collist:
            return True
        else:
            print('collection', col_Name, '不存在')
            return False
    else:
        print('db', db_Name, '不存在')
        return False

def getCol():
    if connect() == True:
        return col
    else:
        return None