from selenium import webdriver
browswer = webdriver.Chrome()

browswer.get("https://github.com/login")

# 정보 획득
from selenium.webdriver.common.by import By
element_login_field = browswer.find_element(by=By.CSS_SELECTOR, value="#login_field") # web element class라는 걸 기억해야 함!
element_login_field.send_keys("adsky0309@gmail.com")

element_password_field = browswer.find_element(by=By.CSS_SELECTOR, value="#password")
element_password_field.send_keys("*")

element_login_button = browswer.find_element(by=By.CSS_SELECTOR, value="div > input.btn.btn-primary.btn-block.js-sign-in-button")
element_login_button.click()

pass

#브라우저 종료
browswer.quit()
