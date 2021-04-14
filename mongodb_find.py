import mongodb_connect

def find_one(where=None, projection=None):
    if mongodb_connect.connect() == True:
        result = mongodb_connect.getCol().find_one(where, projection)
        return result
    else:
        print('find fail')

def find(where=None, projection=None):
    if mongodb_connect.connect() == True:
        results = mongodb_connect.getCol().find(where, projection)
        print('find', results.count(), 'documents')
        return results
    else:
        print('find fail')