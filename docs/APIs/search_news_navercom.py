# 네이버 뉴스
# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests # postman app의 역할을 함

# request api 요청
url = "https://openapi.naver.com/v1/search/news"
params = {'query' : '인공지능'}
headers = {'X-Naver-Client-Id':'ndxIQL5_LTtVAqPe562i','X-Naver-Client-Secret':'V5zNZYCxgr'}
response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

import json
contents = json.loads(response.content)
pass