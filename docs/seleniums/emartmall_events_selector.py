from selenium import webdriver

# chrome 브라우저 옵션 생성
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()


# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36") # 최소한의 정보만 전달함

# WebDriver 생성
browser = webdriver.Chrome(options=chrome_options)

# 주소 입력
for page_number in range(1,7) : #page number
    url = ("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214823&page={}").format(page_number)
    browser.get(url)
    time.sleep(3)
    pass


from selenium.webdriver.common.by import By



browser.quit()



# Chrome 브라우저 옵션 생성


