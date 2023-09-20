import os
import lxml
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By

import smtplib
from email.mime.text import MIMEText     # email 모듈 중 메시지 제목과 본문을 설정하기 위한 라이브러리
from email.mime.multipart import MIMEMultipart  # email 모듈 메일의 데이터 영역의 메시지를 만드는 라이브러리

# dotenv 로드 
load_dotenv(verbose=True)

# 상수 설정 
# Email information
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
SEND_ADRESS_1 = os.getenv("SEND_ADRESS_1")

# 저정가 지정 
SELECT_PRICE = 290

# dirve option 
# fake user 사용 
us = UserAgent(verify_ssl=False)
userAgent = us.random
print(userAgent)

options = uc.ChromeOptions()

# 크롬드라이버 headless 옵션 
options.headless=True
options.add_argument('--headless')   
options.add_argument("--no-sandbox")  

options.add_argument(f'user-agent={userAgent}')  # fake user 설정 
options.add_argument("--load-images=yes")        # 이미지 로드 설정 
options.add_argument("--disable-extensions")     # 비활성화 - 어떤 것을 비활성화 하는지 잘 모르겠음 
options.add_argument("--disable-gpu")            # gpu 가속 사용 제외
options.add_argument("--lang=ja-JP")             # 가짜 플러그인 탑재 - 일본어 설정 
driver = uc.Chrome(options=options)              # 설정된 크롬드라이버 선언

# url 접속 
url = "https://www.amazon.com/SAMSUNG-Monitor-Streaming-Wireless-LS32BM703UNXZA/dp/B09Z2H2JJK/ref=sr_1_6?crid=38WPMAYUTCCU&keywords=samsung%2Btv&qid=1695124000&s=electronics&sprefix=samsung%2Btv%2Celectronics-intl-ship%2C248&sr=1-6&th=1"
driver.get(url)

# 셀레니움에 접속한 url 기준 page source 가져오기
page_source = driver.page_source

# lxml로 파싱하기
soup = BeautifulSoup(page_source, "lxml")

# 데이터 받기 
# 상품명
product = soup.find(class_="a-size-large product-title-word-break").get_text()
product = product.strip()
print(product)

# 가격
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# 크롬드라이버 닫기 
driver.close()
driver.quit()

# 메일 보내기

row_price_check = False

# 조건문 선언 
if price_as_float < SELECT_PRICE:
    row_price_check = True

# 만약 지정가 보다 저가일 경우, 지금 사라고 하는 메일 발송
if row_price_check:
    
    # 메일 본문 작성 - html 형식 
    msg_text =  "안녕하세요.<br>" \
                "<br>" \
                "오늘 아침 9시에 아마존에서,<br>" \
                "<br>" \
                f"{product}를 검색해본 결과<br>" \
                "<br>" \
                "지정된 가격보다 낮아 메일 드립니다.<br>" \
                "<br>" \
                f"구매 링크:{url} 참조 부탁드립니다.<br>" \
                "<br>" \
                "지금 구매하세요!.<br>" \
                "<br>" \
                "가격 트레커 드림<br>" \
    
    # SMTP 서버 접속  
    connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
    connection.starttls()                                           # TLS 암호화 
    connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인
    
    # 수신인 이메일 주소 저장 - 여러 이메일 주소 
    recipients = [MY_EMAIL]
    
    str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
    str_to = ", ".join(recipients)                                   # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
    msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
    
    msg_root["Subject"] = "Hey Amazon!!!"                   # 메일 제목 설정 
    msg_root["From"] = str_from                                        # 보내는 사람 
    msg_root["To"] = str_to                                            # 받는 사람
    msg_alternative = MIMEMultipart('alternative')                     # 메일에 파일을 보내기 위한 MIMEMultipart 객체 생성
    msg_root.attach(msg_alternative)                                   # 선언된 MIMEMultipart 접근 
    msg = MIMEText(msg_text, 'html', _charset="utf8")                  # 메일 본문 내용 작성 
    msg_alternative.attach(msg)                                        # 작성된 메일 본문 접근 
    
    # 지정한 받는 사람 메일주소 별로 내용 전달 
    for recipient in recipients:
        connection.sendmail(
                            from_addr=str_from,                  # 보내는 사람
                            to_addrs=recipient,                  # 받는 사람 
                            msg=msg_root.as_string()             # 메세지 내용
                            )
    
    # SMTP 서버 종료 
    connection.quit()

# 만약 지정가 보다 높다면, 다음에 구매해라라는 메일 보내기 
else:
    # 메일 본문 작성 - html 형식 
    msg_text =  "안녕하세요.<br>" \
                "<br>" \
                "오늘 아침 9시에 아마존에서,<br>" \
                "<br>" \
                f"{product}를 검색해본 결과<br>" \
                "<br>" \
                "지정된 가격보다 아직 높습니다.<br>" \
                "<br>" \
                "감사합니다.<br>" \
                "<br>" \
                "가격 트레커 드림<br>" \
    
    # SMTP 서버 접속  
    connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
    connection.starttls()                                           # TLS 암호화 
    connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인
    
    # 수신인 이메일 주소 저장 - 여러 이메일 주소 
    recipients = [MY_EMAIL]
    
    str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
    str_to = ", ".join(recipients)                                   # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
    msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
    
    msg_root["Subject"] = "Hey Amazon!!!"                   # 메일 제목 설정 
    msg_root["From"] = str_from                                        # 보내는 사람 
    msg_root["To"] = str_to                                            # 받는 사람
    msg_alternative = MIMEMultipart('alternative')                     # 메일에 파일을 보내기 위한 MIMEMultipart 객체 생성
    msg_root.attach(msg_alternative)                                   # 선언된 MIMEMultipart 접근 
    msg = MIMEText(msg_text, 'html', _charset="utf8")                  # 메일 본문 내용 작성 
    msg_alternative.attach(msg)                                        # 작성된 메일 본문 접근 
    
    # 지정한 받는 사람 메일주소 별로 내용 전달 
    for recipient in recipients:
        connection.sendmail(
                            from_addr=str_from,                  # 보내는 사람
                            to_addrs=recipient,                  # 받는 사람 
                            msg=msg_root.as_string()             # 메세지 내용
                            )
    
    # SMTP 서버 종료 
    connection.quit()