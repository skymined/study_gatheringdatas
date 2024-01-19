# 데이터명 공공데이터 포털 : 한국주택금융공사_전세자금대출 금리 정보

import requests 

url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'


params = {'serviceKey' : 'Gc7paAk%2Bpu9XSVXtB0YmE6%2FxA9zA4D8Q%2BfrMBjne9OMNaQdfGSppOtS54DkAhAfYt6Lvx8NUr8ct46cuTNMwtg%3D%3D', 'pageNo' : 1, 'numOfRows' :10, 'dataType':'JSON'}

response = requests.get(url, params=params)

print(response.content)

import json
contents = json.loads(response.content)
# <class
type(contents)

pass

#몽고디비 저장
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient['data_go_kr']
collection = database['rent-loan-rate-info_rate-list']
result = collection.insert_many(contents['body']['items'])