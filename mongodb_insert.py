import mongodb_connect

def insert_one(bson):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().insert_one(bson)
        print('insert success')
    else:
        print('insert fail')

def insert_many(list_bson):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().insert_many(list_bson)
        print('insert success')
    else:
        print('insert fail')