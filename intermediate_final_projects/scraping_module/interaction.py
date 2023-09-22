# interaction.py
from fake_useragent import UserAgent

import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By

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
url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url)

# 문서 개수 추출
document_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(document_count.text)

driver.close()                              # 크롬드라이버 닫기 - 현재 띄워진 단일 탭을 닫는 역할 
driver.quit()                               # 크롬드라이버 종료 - 전체 브라우저 종료