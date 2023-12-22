# auction
# 상품 제목, 판매원가, 변경가격, 배송방법(list)

from selenium import webdriver
browswer = webdriver.Chrome()
browswer.get("https://corners.auction.co.kr/corner/categorybest.aspx")

from selenium.webdriver.common.by import By
selector_value = "div.info"
element_bundle = browswer.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for element_item in element_bundle :
    # 상품 제목
    try:
        element_product_title = element_item.find_element(by=By.CSS_SELECTOR, value="div.info > em > a")
        product_title = element_product_title.text
    except:
        product_title = ""
    print("Title : {}".format(product_title))

    # 판매 원가
    try:
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="li.c_price")
        old_price = element_old_price.text
    except : 
        old_price = ""
    print("Old price : {}".format(old_price))

    # 변경 가격
    try : 
        element_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.sale")
        price = element_price.text
    except:
        price = ""
    print("Price : {}".format(price))

    # 배송방법
    try : 
        element_dilivery = element_item.find_element(by=By.CSS_SELECTOR, value = "div.icon > div")
        dilivery = element_dilivery.text.split()
    except :
        dilivery = ""
    print("Delivery Way : {}".format(dilivery))
    pass