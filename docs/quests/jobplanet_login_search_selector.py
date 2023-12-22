# login 후에 검색어(데이터 분석) 진행

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")

# 정보 입력
from selenium.webdriver.common.by import By
# 이메일 주소 입력창
element_login_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
element_login_field.send_keys("adsky0309@gmail.com")
#비밀번호 입력창
element_password_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
element_password_field.send_keys("*")
pass #패스워드 직접 입력하기 위한 breakpoint 지점
element_login_button = browser.find_element(by=By.CSS_SELECTOR, value="section.section_email.er_r > fieldset > button")
element_login_button.click()

pass
# 브라우저 종료
browser.quit()