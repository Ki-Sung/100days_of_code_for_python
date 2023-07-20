# 매주 월요일 아침 자동으로 명언 이메일로 보내기

# 모듈 불러오기 
import os 
import random
from dotenv import load_dotenv
import datetime as dt 

import smtplib
from email.mime.text import MIMEText     # email 모듈 중 메시지 제목과 본문을 설정하기 위한 라이브러리
from email.mime.multipart import MIMEMultipart  # email 모듈 메일의 데이터 영역의 메시지를 만드는 라이브러리

# dotenv 로드 
load_dotenv(verbose=True)

# 상수 설정 - 각종 정보 
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
SEND_ADRESS_1 = os.getenv("SEND_ADRESS_1")
SEND_ADRESS_2 = os.getenv("SEND_ADRESS_2")

# 요일 설정 - 금일 기준 
now = dt.datetime.now()      # 현재의 날짜와 시각 불러오기 
weekday = now.weekday()      # 요일 불러오기  

# 자동 메일링 실행 코드 
if weekday == 0:                            # 만약 월요일일 경우
    # 명언 데이터 불러오기 
    with open("data/quotes.txt") as data:   # 명언집 데이터 파일을 열고 
        all_quotes = data.readlines()       # 데이터 파일을 한 줄씩 설정 
        quotes = random.choice(all_quotes)   # 랜덤하게 명언 저장 
    
    # 메일 보내기 
    # 메일 본문 작성 - html 형식 
    msg_text =  "월요일 아침이 밝았습니다.<br>" \
                " <br>" \
                "매주 월요일 명언으로 하루를 시작해보는 것은 어떨까요?<br>" \
                "<br>" \
                "금주의 Motivation<br>" \
                f"{quotes}<br>" \
                "<br>" \
                "금주도 활기찬 한 주 되세요!<br>" \
    
    # SMTP 서버 접속  
    connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
    connection.starttls()                                           # TLS 암호화 
    connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인 
    
    # 수신인 이메일 주소 저장 - 여러 이메일 주소 
    recipients = [MY_EMAIL, SEND_ADRESS_1, SEND_ADRESS_2]
    
    str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
    str_to = ", ".join(recipients)                                   # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
    msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
    
    msg_root["Subject"] = "즐거운 월요일 아침이 밝았습니다."                   # 메일 제목 설정 
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

print("전송 완료!")