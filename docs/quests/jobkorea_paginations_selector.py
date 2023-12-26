from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_option = Options()

chrome_option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

browser = webdriver.Chrome(options=chrome_option)
browser.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1")

# 지역 누르기
location_first = browser.find_element(by=By.CSS_SELECTOR, value="#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.loc.circleType.dev-tab.dev-local.on > dd.ly_sub > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child(1) > label > span")
location_second = browser.find_element(by=By.CSS_SELECTOR, value="#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.loc.circleType.dev-tab.dev-local.on > dd.ly_sub > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child(2) > label > span")
location_find = browser.find_element(by=By.CSS_SELECTOR, value="#dev-btn-search")
location_first.click()
location_second.click()
location_find.click()
pass
# 


for page_number in range(1,11) : 
    url = ("https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1{}").format(page_number)
    browser.get(url)
    time.sleep(3)


browser.quit()
