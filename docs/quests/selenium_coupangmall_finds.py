from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.coupang.com/np/search?component=&q=%ED%95%AB%ED%8C%A9&channel=user")

from selenium.webdriver.common.by import By

hotpack_selector_value = "div.name"
hotpack_elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=hotpack_selector_value)

for web_elements in hotpack_elements_path:
    print("{}".format(web_elements.text))

browser.quit()
