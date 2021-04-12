import mongodb_connect

def delete_one(bson):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().delete_one(bson)
        print('delete success')
    else:
        print('delete fail')

def delete_many(bson={}):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().delete_many(bson)
        print('delete success')
    else:
        print('delete fail')