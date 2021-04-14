from flask import Flask, jsonify, request, render_template
import mongodb_find as mongodbfind
import mongodb_insert as mongodbinsert
import mongodb_delete as mongodbdelete
import mongodb_update as mongodbupdate

app = Flask(__name__)

# stores = [
#     {
#         'name': 'Cool Store',
#         'items': [
#             {
#                 'name': 'Cool Item',
#                 'price': 9.99
#             }
#         ]
#     }
# ]

@app.route('/')
def home():
    # return render_template('index.html')
    return 'home'

#取得所有商店
@app.route('/stores')
def get_stores():
    res = mongodbfind.find({}, {'_id':False, 'name':True, 'items':True})
    stores = []
    for i in res:
        stores.append(i)
    return jsonify({'stores': stores})

#新增商店
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    mongodbinsert.insert_one(new_store)
    return jsonify({'name': new_store['name'], 'items': new_store['items']})
    # stores.append(new_store)
    # return jsonify(new_store)

#取得某商店
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    res = mongodbfind.find_one({'name': name}, {'_id':False, 'name':True, 'items':True})
    if res != None:
        return res
    else:
        return jsonify({'message': 'store not found'})

    # for store in stores:
    #     if store['name'] == name:
    #         return jsonify(store)
    # return jsonify({'message': 'store not found'}

#新增某商店內的商品
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    res = mongodbfind.find_one({'name': name}, {'_id':False, 'name':True, 'items':True})
    if res != None:
        items = []
        old_item = res['items']
        new_item = {
                'name': request_data['name'],
                'price': request_data['price']
        }
        items = old_item
        for i in range(0, len(items)):
            if request_data['name'] == items[i]['name']:
                items[i]['price'] = request_data['price']
                break
            else:
                if i == len(items)-1:
                    items.append(new_item)
        where = {'name': name}
        value = {'$set': {'items': items}}
        mongodbupdate.update_one(where, value)
        return jsonify({'name': new_item['name'], 'price': new_item['price']})


        # for item in old_item:
            # if request_data['name'] != item['name']:
            #     items.append(item)
            #     items.append(new_item)
            # else:
            #     items.append(item)
            #     if item['name'] == request_data['name']:
            #         item['price'] = request_data['price']
            # where = {'name': name}
            # value = {'$set': {'items': items}}
            # mongodbupdate.update_one(where, value)
            # return jsonify({'name': new_item['name'], 'price': new_item['price']})
    else:
        return jsonify({'message': 'store not found'})

    # for store in stores:
    #     if store['name'] == name:
    #         new_item = {
    #             'name': request_data['name'],
    #             'price': request_data['price']
    #         }
    #         store['items'].append(new_item)
    #         return jsonify(new_item)
    # return jsonify({'message': 'store not found'})

#取得某商店內的所有商品
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_stoe(name):
    res = mongodbfind.find_one({'name': name}, {'_id':False, 'name':True, 'items':True})
    if res != None:
        return jsonify({'items': res['items']})
    else:
        return jsonify({'message': 'store not found'})

    # for store in stores:
    #     if store['name'] == name:
    #         return jsonify({'items': store['items']})
    # return jsonify({'message': 'store not found'})

#刪除某商店
@app.route('/deletestore/<string:name>', methods=['GET'])
def delete_store(name):
    find_store = mongodbfind.find_one({'name': name})
    if find_store != None:
        res = mongodbdelete.delete_one({'name': name})
        if res == 'success':
            print('1')
            return get_stores()
        else:
            print('2')
            return jsonify({'message': 'delete fail'})
    else:
        return jsonify({'message': 'store not found'})

#刪除某商店內的某商品
@app.route('/store/<string:name>/deleteitem', methods=['POST'])
def delete_item_in_store(name):
    request_data = request.get_json()
    res = mongodbfind.find_one({'name': name}, {'_id':False, 'name':True, 'items':True})
    if res != None:
        items = []
        old_item = res['items']
        delete_item = {
            'name': request_data['name']
        }
        items = old_item
        for i in range(0, len(items)):
            if request_data['name'] == items[i]['name']:
                del items[i]
                where = {'name': name}
                value = {'$set': {'items': items}}
                mongodbupdate.update_one(where, value)
                return get_item_in_stoe(name)
            else:
                if i == len(items)-1:
                    return jsonify({'message': 'item not found'})
    else:
        print('test')
        return jsonify({'messgae': 'store not found'})

# app.run(debug=True)
if __name__ == '__main__':
    app.run()