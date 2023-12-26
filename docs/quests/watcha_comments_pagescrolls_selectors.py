from selenium import webdriver 
browser = webdriver.Chrome()
import time

browser.get("https://pedia.watcha.com/ko-KR/contents/m5ekwXZ/comments")

# - 정보 획득 준비
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body") # body라는 곳의 element 속성을 가지고 옴

previous_scrollHeight = 0
while True : 
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")   ###### 이게 뭐노!!!! ######
    if previous_scrollHeight >= current_scrollHeight :
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(3)
pass

comment_element_body = element_body.find_elements(by=By.CSS_SELECTOR, value="div.css-13j4ly.egj9y8a4")
writers=[]
grades=[]
contents=[]

for x in comment_element_body:
    try:
        writer = x.find_element(by=By.CSS_SELECTOR, value="div.css-eldyae.e10cf2lr1")
        writers.append(writer.text)
    except :
        writers.append("")
    try:
        grade = x.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0 > span")
        grades.append(grade.text)
    except:
        grades.append("")
    try:
        content = x.find_element(by=By.CSS_SELECTOR, value="div.css-2occzs.egj9y8a1 > a > div > span")
        contents.append(content.text)
    except:
        contents.append("")




# 브라우저 종료
browser.quit()

# 얻은 정보들을 mongodb에 넣어봅시다

from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")
database = mongoClient["gatheringdatas"]
watcha_comment_coll = database["watcha_comments"]

for num in range(len(writers)):
    watcha_comment_coll.insert_one({"작성자" : writers[num], "별점":grades[num], "내용":contents[num]})
