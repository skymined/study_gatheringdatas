from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://getbootstrap.com/docs/5.3/examples/checkout/")
from selenium.webdriver.common.by import By
import time



# 정보 획득
from selenium.webdriver.support.ui import Select
# Select(driver.find_element(By.TAG_NAME, “select”)).select_by_index(2)
# 국가 selectbox 선택
selector_element = '#country'
element_country = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_country).select_by_index(1)

# 주 selectbox 선택
selector_element = '#state'
element_state = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_state).select_by_index(1)



browser.quit()