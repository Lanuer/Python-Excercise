import mongodb_connect

def update_one(where, value):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().update_one(where, value)
        print('update success')
    else:
        print('update fail')

def update_many(where, value):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().update_many(where, value)
        print('update success', result.modified_count, 'documents')
    else:
        print('update fail')