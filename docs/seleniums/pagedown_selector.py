# * 웹 크롤링 동작
from selenium import webdriver # 안에 클래스가 많아서 다 가지고 와야 함 webdriver가 브라우저와 유사한 행동을 함

# - chrome browser 열기
browser = webdriver.Chrome()  # class는 chrome으로 처음 생성하는 것 class의 생성자 class의 모든 자원이 return됨
import time

# - 주소 https://www.w3schools.com/ 입력
browser.get(str("https://www.w3schools.com/"))


# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## 한 페이지씩 이동
element_body = browser.find_elements(by=By.CSS_SELECTOR, value="body") # body라는 곳의 element 속성을 가지고 옴
element_body.send_keys(Keys.PAGE_DOWN)
element_body.send_keys(Keys.PAGE_DOWN)

element_body.send_keys(Keys.PAGE_UP)
element_body.send_keys(Keys.PAGE_UP)

# 브라우저 종료
browser.quit()

