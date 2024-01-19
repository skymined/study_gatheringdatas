# 데이터명 공공데이터 포털 : 기상청_관광코스별 관광지 상세 날씨 조회서비스

import requests

url  = "http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1"
params = {'serviceKey' : 'Gc7paAk%2Bpu9XSVXtB0YmE6%2FxA9zA4D8Q%2BfrMBjne9OMNaQdfGSppOtS54DkAhAfYt6Lvx8NUr8ct46cuTNMwtg%3D%3D', 'pageNo' : 1, 'numOfRows':10, 'dataType':'JSON', "CURRENT_DATE":2018123110, 'DAY':3, 'CITY_AREA_ID' : 5013000000}

response = requests.get(url, params=params)

import json
contents = json.loads(response.content)

from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient['data_go_kr']
collection = database['TourStnInfoService1']
result = collection.insert_many(contents['response']['body']['items']['item'])