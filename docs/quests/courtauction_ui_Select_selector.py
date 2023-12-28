# 웹 크롤링 기본 세팅
from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 몽고디비 기본 세팅
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient["gatheringdatas"]
coll_court_location = database['courtauction_ui_select']
coll_court_location.delete_many({})


# 경매 마당 
def court(coll_court_location):
    for x in (3,5,9,11):
        browser.find_element(by=By.CSS_SELECTOR, value='#menu > h1:nth-child(5) > a').click() #경매 물건 검색
        location_options = browser.find_element(by=By.CSS_SELECTOR, value='#idJiwonNm')
        location_list = browser.find_element(by=By.CSS_SELECTOR, value='#idJiwonNm').text.split() # 법원 option들 리스트화
        Select(location_options).select_by_value(location_list[x]) # 법원 index 내 검색 후
        location_option = location_list[x]
        browser.find_element(by=By.CSS_SELECTOR, value='#contents > form > div.tbl_btn > a:nth-child(1)').click() # 검색 버튼 클릭
        time.sleep(2)

        
        for y in(2,4,5,6,7,8,9,10,11):
            courtscrapping(location_option, coll_court_location)
            try:
                note = ("#contents > div > form > div > div.page2 > a:nth-child({})").format(y)
                browser.find_element(by=By.CSS_SELECTOR, value=note).click()
            except :
                break
        pass


def courtscrapping(location_option, coll_court_location) : 
    case_boxs = browser.find_elements(by=By.CSS_SELECTOR, value='#contents > div.table_contents > form > table > tbody > tr')
    for case_box in case_boxs :
        case_num = case_box.find_element(by=By.CSS_SELECTOR, value='form > table > tbody > tr > td:nth-child(2)').text # 사건 번호
        location_contents = list(case_box.find_elements(by=By.CSS_SELECTOR, value='form > table > tbody > tr> td:nth-child(4) > div'))
        for x in range(len(location_contents)) :
            location_content = location_contents[x]
            coll_court_location.insert_one({"법원 소재지":location_option,
                                            "사건 번호" : case_num,
                                            "소재지 및 내역" : location_content.text})
            pass
# 코딩 돌리기
               
browser.get("https://www.courtauction.go.kr/")
time.sleep(2)
browser.switch_to.frame('indexFrame')

court(coll_court_location)

browser.quit()
