# 스크래핑 기본 세팅
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.11st.co.kr/products/5814478973?trTypeCd=22&trCtgrNo=895019")
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 몽고디비 기본 세팅
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient["gatheringdatas"]
comments_11st_coll = database["11st_comments"]

# 리뷰 버튼 누르기
browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
browser.switch_to.frame("ifrmReview")

# 더보기 버튼 끝까지 누르기
page = 0
while True :
    try:
        Button = browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button")
        Button.click()
        page += 1
        time.sleep(2)
    except NoSuchElementException :
        break

pass
# 리뷰 스크래핑하기 (작성자, 선택 옵션, 별점, 내용)
writers = []
options = []
grades = []
contents =[]

for page_num in range(1,page+2) :
    for num_num in range(1,11):
        # 작성자
        try :
            writer_value = ("#review-list-page-area > ul:nth-child({}) > li:nth-child({}) > dl > dt").format(page_num, num_num)
            writers.append(browser.find_element(by=By.CSS_SELECTOR, value=writer_value).text)
        except NoSuchElementException:
            break

        # 선택 옵션
        try :  
            option_value_1_way = ("ul:nth-child({}) > li:nth-child({}) > div > dl > div").format(page_num, num_num)
            options.append(browser.find_element(by=By.CSS_SELECTOR, value=option_value_1_way).text)
        except NoSuchElementException :
            try:
                option_value_2_way = ("ul:nth-child({}) > li:nth-child({}) > div > p.option").format(page_num, num_num)
                options.append(browser.find_element(by=By.CSS_SELECTOR, value=option_value_2_way).text)
            except NoSuchElementException:
                options.append("")

        # 별점
        try : 
            grade_value = ("ul:nth-child({}) > li:nth-child({}) > div > p.grade > span > em").format(page_num, num_num)
            grades.append(browser.find_element(by=By.CSS_SELECTOR, value=grade_value).text)    
        except NoSuchElementException :
            grades.append("")

        # 내용
        try : 
            content_value=("ul:nth-child({}) > li:nth-child({}) > div > div > div.cont_text_wrap > p").format(page_num, num_num)
            contents.append(browser.find_element(by=By.CSS_SELECTOR, value=content_value).text)           
        except NoSuchElementException :
            contents.append("")



# mongodb에 내용 넣기
comments_11st_coll.delete_many({})
for x in range(len(writers)) :
    comments_11st_coll.insert_one({"작성자":writers[x], "선택 옵션":options[x], "별점" : grades[x], "내용":contents[x]})
pass