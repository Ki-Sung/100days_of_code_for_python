# 생일 메시지 자동 메일링 프로젝트 

# 모듈 불러오기 
import os 
import random
import pandas as pd 
from dotenv import load_dotenv
from datetime import datetime

import smtplib
from email.mime.text import MIMEText     # email 모듈 중 메시지 제목과 본문을 설정하기 위한 라이브러리
from email.mime.multipart import MIMEMultipart  # email 모듈 메일의 데이터 영역의 메시지를 만드는 라이브러리

# dotenv 로드 
load_dotenv(verbose=True) 

MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")

# datetime으로 현재 데이터 불러오기 - 월, 일 
today = (datetime.now().month, datetime.now().day)

# 데이터 프레임으로 csv 파일 불러오기 
data = pd.read_csv("./data/birthdays.csv")

# 데이터 프레임 내 데이터를 딕셔너리로 변환 - 컴프리핸션 사용 
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

# 실제 구동 코드 
if today in birthday_dict:                                                  # 만약 딕셔너리에 금일자 데이터에 대한 데이터가 있다면 
    birthday_person = birthday_dict[today]                                  # 생일자 저장 
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"      # 이메일 본문 탬플릿 걍로 (템플릿 3개 중 랜덤으로 설정)
    with open(file_path) as letter_file:                                    # 설정된 경로를 with 문으로 
        contents = letter_file.read()                                       # 설정된 경로로 탬플릿 열기 
        contents = contents.replace("[NAME]", birthday_person["name"])      # 맨위 생알자 이름을 바꿔주기 
    
    # 메일 보내기     
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:                 # SMTP 서버 접속 
        connection.starttls()                                               # TLS 암호화 
        connection.login(MY_EMAIL, GOOGLE_APP_PASSWORD)                     # SMTP 로그인 
        connection.sendmail(                                                # 메일 보내기 
                            from_addr=MY_EMAIL,                             # 보내는 사람 
                            to_addrs=birthday_person["email"],              # 받는 사람
                            msg= f"Subject: Happy Birthday!\n\n{contents}"  # 메일 메시지 내용 설정
                            )
