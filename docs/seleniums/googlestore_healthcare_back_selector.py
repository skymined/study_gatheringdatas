# * 웹 크롤링 동작
from selenium import webdriver # 안에 클래스가 많아서 다 가지고 와야 함 webdriver가 브라우저와 유사한 행동을 함
browser = webdriver.Chrome()
browser.get("https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR&pli=1")

import time

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 앱 제조회사 리스트 : div > 
element_companys = browser.find_elements(by=By.CSS_SELECTOR, value="div > a.Si6A0c.Gy4nib")
for company in element_companys :
    company.click()
    time.sleep(1)
    element_title = browser.find_element(by=By.CSS_SELECTOR, value= "div > h1")
    print("App company Name : {}".format(element_title.text))
    browser.back() #브라우저에서 back할 수 있게 하는 것. 제품 리스트로 이동
    time.sleep(2)
    pass

# 브라우저 종료
browser.quit()

