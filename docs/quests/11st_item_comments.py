# 스크래핑 기본 세팅
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.11st.co.kr/browsing/DealBest.tmall?method=getShockingDealBestMain&dispCtgrNo=947169&dbCacheUse=N")
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 몽고 디비 연결
from pymongo import MongoClient
mongo = MongoClient("mongodb://localhost:27017")
database = mongo["gatheringdatas"]
coll_11st_items = database["11st_item"]
coll_11st_item_comments = database["11st_item_comments"]
coll_11st_items.delete_many({})
coll_11st_item_comments.delete_many({})

# 상품상세 정보와 리뷰 크롤링(명칭, image link, 원가, 판매가, 상품정보)

def item_infor() :
    while True :
        browser.find_element(by=By.CSS_SELECTOR, value="div > ul > li > div >a").click() # 항목들 클릭
        time.sleep(1)
        # 클릭해서 들어간 곳의 상세 정보 스크래핑
        element_name = browser.find_element(by=By.CSS_SELECTOR, value="div.c_product_info_title.c_product_info_title_coupon > h1")
        try : # 이미지 : #productImg > div > img
            element_image = browser.find_element(by=By.CSS_SELECTOR, value="#productImg > div > img").get_attribute('src')
        except :
            element_image = "None"
        try : # 원가 
            element_price = browser.find_element(by=By.CSS_SELECTOR, value="div > div > dl > div > dd > del")
        except :
            element_price ='None'
        try : # 판매가
            element_sale = browser.find_element(by=By.CSS_SELECTOR, value="#finalDscPrcArea > dd.price > strong")
        except : 
            element_sale = 'None'
        try : # 상품정보
            browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail1").click()
            time.sleep(1)
            element_infor = browser.find_element(by=By.CSS_SELECTOR, value="#tabpanelDetail1 > table > tbody")
        except :
            element_infor = 'None'

        result = coll_11st_items.insert_one({"이름":element_name.text,
            "이미지 링크" :element_image,
            "원가":element_price.text,
            "판매가" : element_sale.text,
            "상품정보" :element_infor.text})

        # 리뷰 스크래핑하기
        browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
        browser.switch_to.frame("ifrmReview")
        try :
            element_body = browser.find_elements(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li")
            for element_item in element_body :
                try : # 작성자 
                    comment_name = element_item.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li> dl > dt")
                except NoSuchElementException :
                    comment_name = 'None'
                try : # 선택옵션
                    comment_option = element_item.find_element(by=By.CSS_SELECTOR, value='#review-list-page-area > ul > li > div > dl > div >dd')
                except NoSuchElementException :
                    try : 
                        comment_option =element_item.find_element(by=By.CSS_SELECTOR, value='#review-list-page-area > ul > li > div > p.option')
                    except NoSuchElementException :
                        comment_option ='None'
                try : #별점
                    comment_grade = element_item.find_element(by=By.CSS_SELECTOR, value='#review-list-page-area > ul > li> div > p.grade > span > em')
                except NoSuchElementException :
                    comment_grade ='None'
                try : # 내용
                    comment_content = element_item.find_element(by=By.CSS_SELECTOR, value = '#review-list-page-area > ul > li > div > div > div.cont_text_wrap > p')
                except NoSuchElementException :
                    comment_content = 'None'
        except NoSuchElementException :
            pass

        # 몽고디비에 정보 넣기

        item_id = result.inserted_id
        try :
            coll_11st_item_comments.insert_one({"상품ID":item_id,
                                            "리뷰 작성자":comment_name.text,
                                            "리뷰 선택옵션":comment_option.text,
                                            "리뷰 별점" : comment_grade.text,
                                            "리뷰 내용":comment_content.text})
        except UnboundLocalError :
            break
        browser.back()
        time.sleep(2)
        if NoSuchElementException :
            pass



item_infor()
browser.quit()
