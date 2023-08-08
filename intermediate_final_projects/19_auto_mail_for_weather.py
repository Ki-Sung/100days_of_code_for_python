# 모듈 불러오기 
import os 
import random
from dotenv import load_dotenv
import datetime as dt 
import requests

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
OWM_API_KEY = os.getenv("OWM_API_KEY")

# Open Weather API Information
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"   # Endpoint URL 

# Open Weather Parameters 
weather_params = {
    "lat":  37.541,        # 서울 위도값 
    "lon": 126.986,        # 서울 경도값 
    "appid": OWM_API_KEY,  # API Key
    "exclude": "current,minutely,daily"  # 제외할 파라미터 값
}

response = requests.get(OWM_Endpoint, params=weather_params)      # 앤드포인트로 요청 받기
response.raise_for_status()                                       # 응답 코드 - 200이 아니면 예외를 발생 시킴

weather_data = response.json()                                            # 200을 받으면 JSON 형식으로 데이터 받기 

weather_slice = weather_data["hourly"][:12]                      # 12시간의 날씨 데이터 호출

will_rain = False        # 프린트문을 여러차례 호출하지 않게 하기 위

# 반복문으로 날씨 상태 ID 값 추출
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]   # 0부터 11까지 시간의 날씨 코드 추출
    
    # 조건문 선언
    if int(condition_code) < 700:     # 만약 날씨 코드가 700 미만이면 
        will_rain = True              # True로 반환 (즉 하나라도 해당 조건의 값이 있으면 True로 반환)
        
# 결과 출력 
if will_rain:                   # 만약 조건의 값이 성립 되먄(즉 True일 경우)
    # 메일 보내기 
    # 메일 본문 작성 - html 형식 
    msg_text =  "아침이 밝았습니다. .<br>" \
                "<br>" \
                "오늘 아침 7시부터 저녁 7시 사이,<br>" \
                "<br>" \
                "비가 예보되어 있으니 꼭 우산을 챙기시기 바랍니다! ☔<br>" \
                "<br>" \
                "그럼 오늘도 힘찬 하루 시작해볼까요?<br>" \
                "<br>" \
                "감사합니다.<br>" \
                "<br>" \
                "비 예보 시스템 드림<br>" \
    
    # SMTP 서버 접속  
    connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
    connection.starttls()                                           # TLS 암호화 
    connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인 
    
    # 수신인 이메일 주소 저장 - 여러 이메일 주소 
    recipients = [MY_EMAIL, SEND_ADRESS_1, SEND_ADRESS_2]
    
    str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
    str_to = ", ".join(recipients)                                   # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
    msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
    
    msg_root["Subject"] = "오늘 비 예보가 있으니, 우산을 챙기시기 바랍니다. ☔"                   # 메일 제목 설정 
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
    
else:
    # 메일 보내기 
    # 메일 본문 작성 - html 형식 
    msg_text =  "아침이 밝았습니다. .<br>" \
                "<br>" \
                "오늘 아침 7시부터 저녁 7시 사이,<br>" \
                "<br>" \
                "비소식은 없습니다. <br>" \
                "<br>" \
                "그럼 오늘도 힘찬 하루 시작해볼까요?<br>" \
                "<br>" \
                "감사합니다.<br>" \
                "<br>" \
                "비 예보 시스템 드림<br>" \
    
    # SMTP 서버 접속  
    connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
    connection.starttls()                                           # TLS 암호화 
    connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인 
    
    # 수신인 이메일 주소 저장 - 여러 이메일 주소 
    recipients = [MY_EMAIL, SEND_ADRESS_1, SEND_ADRESS_2]
    
    str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
    str_to = ", ".join(recipients)                                   # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
    msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
    
    msg_root["Subject"] = "금일은 비가 오지 않을 전망입니다."                 # 메일 제목 설정 
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