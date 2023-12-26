# * 웹 크롤링 동작
from selenium import webdriver # 안에 클래스가 많아서 다 가지고 와야 함 webdriver가 브라우저와 유사한 행동을 함

# - chrome browser 열기
browser = webdriver.Chrome()  # class는 chrome으로 처음 생성하는 것 class의 생성자 class의 모든 자원이 return됨

# - 주소 https://www.w3schools.com/ 입력
browser.get(str("https://emart.ssg.com/search.ssg?target=all&query=%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC"))

# - 가능 여부에 대한 OK 받음
pass


# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div.mnemitem_unit.gate_unit"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for element_item in element_bundle :
    # print(element_item.text) # 상품정보들
    # 상품 제목
    # element_title = element_item.find_element(by=By.CSS_SELECTOR, value="div.mnemitem_goods_tit") # 이건 아직 tag 상태이기 때문에 .text를 이용해서 텍스트로 바꿔주어야 함
    # print("title : {}".format(element_title.text))
    # 상품 판매 원가

    try:
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="div > del > em")
        old_price = element_old_price.text
        pass
    except:
        old_price="" # 값이 없을 경우에 그냥 빈공간으로 내뱉을 수 있도록 해줌
        pass
    finally:
        pass
    
    print("old price : {}".format(old_price))


# 브라우저 종료
browser.quit()

