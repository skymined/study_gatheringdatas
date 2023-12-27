# 스크래핑 기본 세팅
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.11st.co.kr/browsing/DealBest.tmall?method=getShockingDealBestMain&dispCtgrNo=947169&dbCacheUse=N")
import time
from selenium.webdriver.common.by import By

# 몽고 디비 연결
from pymongo import MongoClient
mongo = MongoClient("mongodb://localhost:27017")
database = mongo["gatheringdatas"]
coll_11st_items = database["11st_item"]
coll_11st_item_comments = database["11st_item_comments"]

# 상품상세 정보와 리뷰 크롤링(명칭, image link, 원가, 판매가, 상품정보)

def item_infor() :
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="div > ul > li > div >a")
    for element in elements :
        browser.find_element(by=By.CSS_SELECTOR, value="div > ul > li > div >a") # 항목들 클릭
        # 클릭해서 들어간 곳의 상세 정보 스크래핑
        try :
            element_name = browser.find_element(by=By.CSS_SELECTOR, value="div.c_product_info_title.c_product_info_title_coupon > h1").text
        except :
            element_name = ""
        try : # 이미지 : #productImg > div > img
            element_image = browser.find_element(by=By.CSS_SELECTOR, value="#productImg > div > img")
        except :
            element_image = ""
        try : # 원가
            element_price = browser.find_element(by=By.CSS_SELECTOR, value="#layBodyWrap > div > div.s_product.s_product_detail.fixed > div.l_product_cont_wrap > div > div.l_product_view_wrap > div.l_product_summary > div.l_product_side_info > div.b_product_info_price.b_product_info_price_style2 > div > div > dl > div:nth-child(1) > dd")
        except :
            element_price =''
        try : # 판매가
            element_sale = browser.find_element(by=By.CSS_SELECTOR, value="#finalDscPrcArea > dd.price > strong")
        except : 
            element_sale = ''
        try : # 상품정보
            browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail1").click()
            element_infor = browser.find_element(by=By.CSS_SELECTOR, value="#tabpanelDetail1")
        except :
            element_infor = ''
        # 리뷰 스크래핑하기
        


        
    #mongodb에 데이터 집어넣기
            
