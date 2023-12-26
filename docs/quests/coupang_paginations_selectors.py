from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Chrome WebDriver 경로 설정
chrome_driver_path = '/path/to/chromedriver'

# Chrome WebDriver 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 실행
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
browser.get("https://www.coupang.com/np/search?component=&q=%EB%82%9C%EB%A1%9C&channel=user")

for page_number_coupang in range(1,11):
    url = ("https://www.coupang.com/np/search?q=%EB%82%9C%EB%A1%9C&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=9&backgroundColor=").format(page_number_coupang)
    browser.get(url)
    time.sleep(3)
    pass



browser.quit()