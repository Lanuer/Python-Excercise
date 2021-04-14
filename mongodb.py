from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId
import datetime
import mongodb_find as mongofind
import mongodb_insert as mongoinsert
import mongodb_delete as mongodelete
import mongodb_update as mongoupdate

#連線
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb+srv://lanuer:zaq123456@realmcluster.6fpkj.mongodb.net/lanuer_mongo?retryWrites=true&w=majority')
#DB名稱
db = client['test-database']
#Collection名稱
collection = db['test-collection']

#查詢某DB是否存在
db_Name = 'test-database'
dblist = client.list_database_names()
if db_Name in dblist:
    print('您的DB: {0}存在'.format(db_Name))
print('目前存在的collection有', db.list_collection_names())
#查詢某collection是否存在
col_Name = 'test-collection'
collist = db.list_collection_names()
if col_Name in collist:
    print('您的collection {0} 存在'.format(col_Name))

#資料
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

mydict = {'name':'Lanuer', 'says':'Hello 你好嗎?'}
mylist = [
    {'name':'Lanuer1','says':'says1'},
    {'name':'Lanuer2','says':'says2'},
    {'name':'Lanuer3','says':'says3'},
    {'name':'Lanuer4','says':'says4'},
    {'name':'Lanuer5','says':'says5'},
    {'name':'Lanuer6','says':'says6'},
    {'name':'Lanuer7','says':'says7'}
]

#Test
# result = collection.create_index([('user_id', pymongo.ASCENDING)], unique=True)
# sorted(list(collection.index_information()))
value = [
    {'name':'Lanuer', 'age':20},
    {'name':'Lanuer2', 'age':20}
]

# x = collection.insert_one(mydict) #插入單筆資料
# print('插入單筆成功')
# y = collection.insert_many(mylist) #插入多筆資料
# print('插入多筆成功 返回_id值', y.inserted_ids)

#insert資料
# post_id = collection.insert_one(post).inserted_id
# print ("post id is ", post_id)

# cur_collection = db.collection_names(include_system_collections=False)
# print('cur_collection is :', cur_collection)

#find單筆資料
# x = collection.find_one()
# x = collection.find_one({'name':'Lanuer'})
# x = collection.find_one({'_id': ObjectId('')})
# print(x)
#find全部資料所有欄位
# res = collection.find()
# res = collection.find({'age':'20'})
# for y in res:
#     print(y)
#find全部資料某欄位json格式
# res = collection.find({}, {'_id':False, 'name':True})
# for x in res:
#     print(x)
#find全部資料部分欄位str格式
res = collection.find()
for x in res:
    print(x['name']) #純value
    # print(f"name={x['name']}") #自定義value
#用ObjectId查資料
# value = {'_id': ObjectId('6064590574dd0b38b766dde6')}
# res = mongofind.find_one(value)
# print(res)
#查詢有幾條
# count = collection.find().count()
# print(count)

#update單筆資料
# where = {'name':'Lanuer'}
# res = {'$set':{'age':25}}
# result = collection.update_one(where, res)
# print(result)
#update多筆資料
# where = {'name':{'$regex':'Lanuer'}}
# res = {'$set':{'age':18}}
# result = collection.update_many(where, res)
# print(result.modified_count, 'documents updated.')

#delete單筆資料
# result = {'name':'Lanuer2'}
# collection.delete_one(result)
# print('成功刪除')
#delete多筆資料
# result = {'name':{'$regex':'Lanuer'}}
# x = collection.delete_many(result)
# print(x.deleted_count, ' documents deleted.')
#delete全部資料
# x = collection.delete_many({})
# print(x.deleted_count, ' documents deleted.')