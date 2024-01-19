# 주소 https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91

def getapi():
    import requests
    url = "https://openapi.naver.com/v1/search/shop"
    params = {'query':'자이로'}
    headers = {'X-Naver-Client-Id':'ndxIQL5_LTtVAqPe562i','X-Naver-Client-Secret':'V5zNZYCxgr'}
    response = requests.get(url, params=params, headers=headers)

    import json
    shop_contents = json.loads(response.content)
    return shop_contents

# 몽고디비에 아이템 넣기

def put_to_mongo(collection1, collection2, shop_contents) : 
    from pymongo import MongoClient
    mongoclient = MongoClient("mongodb://localhost:27017")
    database = mongoclient['data_go_kr']
    shop_info = database[collection1]
    shop_list = database[collection2]
    shop_info.delete_many({})
    shop_list.delete_many({})
    result = shop_info.insert_one({'lastBuildDate' : shop_contents['lastBuildDate'], 'total':170641, 'start':1, 'display':10})
    id_relative = result.inserted_id

    for i in shop_contents['items'] :
        i['id_relative'] = id_relative
    
    shop_list.insert_many(shop_contents['items'])


shop_contents = getapi()
put_to_mongo('search_shop_info', 'search_shop_list', shop_contents)

