# 클릭을 많이 하면 높은 점수를 얻는 쿠키 게임을 자동으로 클릭하게 하는 쿠키봇
# 전체 코드 
import time
from fake_useragent import UserAgent

import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# fake user 사용 
us = UserAgent(verify_ssl=False)
userAgent = us.random
print(userAgent)

# 크롬드라이버 옵션 선언
options = uc.ChromeOptions()

# 크롬드라이버 headless 옵션 
# options.headless=True
# options.add_argument('--headless')   
options.add_argument("--no-sandbox")  

options.add_argument(f'user-agent={userAgent}')  # fake user 설정 
options.add_argument("--load-images=yes")        # 이미지 로드 설정 
options.add_argument("--disable-extensions")     # 비활성화 - 어떤 것을 비활성화 하는지 잘 모르겠음 
options.add_argument("--disable-gpu")            # gpu 가속 사용 제외
options.add_argument("--lang=ja-JP")             # 가짜 플러그인 탑재 - 일본어 설정 
driver = uc.Chrome(options=options)              # 설정된 크롬드라이버 선언

# url 설정 
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

# 쿠키 엘리먼츠 찾기
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

# 업그레이드할 아이템 id 값 저장
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

# 시간 설정
timeout = time.time() + 5      # 타임아웃 5초 설정
five_min = time.time() + 60*5  # 총 게임 오토봇 사용시간 설정 (5분)

while True:
    # 쿠키 클릭
    cookie.click()
    
    # 매 5초 간
    if time.time() > timeout:
        # 업그레이드를 위해 모든 아이템 가격 추출을 위한 가격 요소들 추출
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

        # 모든 아이템 가격 정보 추출 
        item_prices = []

        for price in all_prices:
            element_text = price.text            # 가격 요소의 Text 추출 
            if element_text != "":               # 추출된 Text 중 ""빈 문자열이 끝에 있어 조건문 제시 
                cost = int(element_text.split("-")[1].strip().replace(",", ""))  # 문자열 구분자로 숫자만 추출 후 정수형으로 데이터 타입 변경
                item_prices.append(cost)         # 빈 리스트에 저장   
        
        # 아이템명:가격 형식으로 딕셔너리 생성
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
            
        
        # 현재 쿠키 개수 추출 
        money_element = driver.find_element(By.ID, "money").text  # 현재 쿠키 개수 추출
        if "," in money_element:                                  # 만약 숫자 사이에 구분자 ","가 있다면 
            money_element = money_element.replace(",", "")        # "," 제거 
        cookie_count = int(money_element)                         # 문자열을 정수형으로 변경
        
        # 현재 쿠키 개수로 구매할 수 있는 아이템
        affordable_upgrades = {}
        for cost, item_id in cookie_upgrades.items():    # cost와 item_id를 반복문을 통해서 저장 
            if cookie_count > cost:                      # 만약 현재 쿠키가 아이템 cost 보다 클 경우 (즉 충분한 쿠기가 있을 경우)
                affordable_upgrades[cost] = item_id      # affordable_upgrades에 딕녀서리 형식으로 저장
                
        # 가장 비싼 업그레이드 하기
        highest_price_affordable_upgrade = max(affordable_upgrades)             # 지금 살수 있는 아이템중 가장 비싼 가격 추출
        print(highest_price_affordable_upgrade)                                 # 가격 추출
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]  # 해당 가격의 아이템 추출
        
        # 추출한 아이템 클릭 
        driver.find_element(By.ID, to_purchase_id).click()
        
        # 다음 확인까지 5초 추가
        timeout = time.time() + 5
        
    # 5분이 지난 후 봇 종료, 종료와 동시에 얻은 쿠키의 개수 추출 
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
        
driver.close()                              # 크롬드라이버 닫기 - 현재 띄워진 단일 탭을 닫는 역할 
driver.quit()                               # 크롬드라이버 종료 - 전체 브라우저 종료