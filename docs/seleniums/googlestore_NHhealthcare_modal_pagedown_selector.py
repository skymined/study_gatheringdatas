from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://play.google.com/store/apps/details?id=com.nhlife.customer.healthcare&hl=ko-KR&pli=1")
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# 모달 화면 띄우기 : 평가 및 리뷰 클릭
browser.find_element(by=By.CSS_SELECTOR, value='c-wiz:nth-child(4) > section > header > div > div:nth-child(2) > button').click()
time.sleep(1)

# 댓글 모달 확인 : (css overflow:scroll or auto) : div.fysCi
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value='div.fysCi')

# 댓글 마지막까지 스크롤 
previous_scrollHeight = 0
while True:
    # python 방식 변수 매칭
    print("{0}.scrollTo({1}, {0}.scrollHeight);".format(element_scrollableDiv, previous_scrollHeight))

    # javascipt와 python 결합 방식 변수 매칭
    browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);"
                           ,element_scrollableDiv, previous_scrollHeight)

    current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight",
                                                  element_scrollableDiv)
    
    if previous_scrollHeight >= current_scrollHeight:
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass



# 댓글 개수 확인 :
reviews = browser.find_elements(by=By.CSS_SELECTOR, value='div.RHo1pe')
print ("Count comment before done scroll : {}".format(len(reviews)))

browser.quit()