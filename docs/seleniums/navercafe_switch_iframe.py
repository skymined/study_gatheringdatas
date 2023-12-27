from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://cafe.naver.com/peopledisc")
import time
from selenium.webdriver.common.by import By # 정보 획득을 위한 모듈

# 병원 진료 후기 메뉴 클릭 : #menuLink84
browser.find_element(by=By.CSS_SELECTOR, value="#menuLink84").click()

# iframe으로 전환
browser.switch_to.frame('cafe_main') # name을 사용해서 접근한 것


# 해당 리스트를 가지고 오기
cafe_list = browser.find_elements(by=By.CSS_SELECTOR, value="#main-area > div:nth-child(4) > table > tbody > tr")
pass

browser.quit()