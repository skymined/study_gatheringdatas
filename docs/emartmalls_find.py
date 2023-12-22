# * 웹 크롤링 동작
from selenium import webdriver # 안에 클래스가 많아서 다 가지고 와야 함 webdriver가 브라우저와 유사한 행동을 함

# - chrome browser 열기
browser = webdriver.Chrome()  # class는 chrome으로 처음 생성하는 것 class의 생성자 class의 모든 자원이 return됨

# - 주소 입력
browser.get(str("https://emart.ssg.com/search.ssg?target=all&query=%EC%9A%B4%EB%8F%99%EC%9A%A9%ED%92%88"))

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득 # selecter 방법을 이용할 것. 어떤 element로 find할 것인지 두 가지 parameter가 들어감
from selenium.webdriver.common.by import By

## 하나의 element만 가지고 오기
selector_value = "#item_unit_1000287252141 > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
element_path = browser.find_element(by=By.CSS_SELECTOR, value=selector_value) # class를 return 한 것. 이거 이해할 필요가 있을 듯. class를 return한다는 게 무슨 뜻인지
# get text in tag  # tag 안에 있는 text를 가지고 오는 방법
element_path.text
pass

## 여러 개의 element 정보 가지고 오기
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
pass

type(elements_path)
# <class 'list'>

type(elements_path[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'> class 종류가 web elements
elements_path[0].text
#'좌식 실내자전거 704R 온가족 헬스자전거'
elements_path[1].text
# '[SSG특가]엑스바이크 메타 가정용 실내자전거 즈위프트 센서 사이클 게임'

for web_elements in element_path :
    title = web_elements.text
    print("{}".format(title))
    pass


# 브라우저 종료
browser.quit()

