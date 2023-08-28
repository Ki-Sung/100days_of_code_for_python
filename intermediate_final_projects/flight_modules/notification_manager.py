# 모듈 불러오기 
import os 
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText     # email 모듈 중 메시지 제목과 본문을 설정하기 위한 라이브러리
from email.mime.multipart import MIMEMultipart  # email 모듈 메일의 데이터 영역의 메시지를 만드는 라이브러리

# dotenv 로드 
load_dotenv(verbose=True)

# 상수 설정 - 각종 정보 
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
SEND_ADRESS_1 = os.getenv("MY_EMAIL")
SEND_ADRESS_2 = os.getenv("SEND_ADRESS_2")

# 메일 서비스를 위한 클래스
class NotificationManager:
    def __init__(self):
        # SMTP 서버 접속  
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)                # SMTP 서버 연결 시작 
        self.connection.starttls()                                           # TLS 암호화 
        self.connection.login(user=MY_EMAIL, password=GOOGLE_APP_PASSWORD)   # SMTP 로그인 
        
    def send_mail(self, msg_text):
        self.recipients = [SEND_ADRESS_1, SEND_ADRESS_2]                      # 메일로 보낼 주소 입력 
        self.str_from = MY_EMAIL                                              # 보내는 사람의 메일 주소 
        self.str_to = ", ".join(self.recipients)                              # 받는 사람의 메일 주소 - 여러 메일 주소 설정 
        self.msg_root = MIMEMultipart("related")                              # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
        
        self.msg_root["Subject"] = "현재까지 검색된 최저가 항공 가격입니다."                   # 메일 제목 설정 
        self.msg_root["From"] =  self.str_from                                       # 보내는 사람 
        self.msg_root["To"] = self.str_to                                            # 받는 사람
        self.msg_alternative = self.MIMEMultipart('alternative')                          # 메일에 파일을 보내기 위한 MIMEMultipart 객체 생성
        self.msg_root.attach(self.msg_alternative)                                   # 선언된 MIMEMultipart 접근 
        self.msg = self.MIMEText(msg_text, 'html', _charset="utf8")                  # 메일 본문 내용 작성 
        self.msg_alternative.attach(self.msg)                                        # 작성된 메일 본문 접근 
        
        # 지정한 받는 사람 메일주소 별로 내용 전달 
        for recipient in self.recipients:
            self.connection.sendmail(
                                from_addr=self.str_from,                  # 보내는 사람
                                to_addrs=self.recipient,                  # 받는 사람 
                                msg=self.msg_root.as_string()             # 메세지 내용
                                )
        
        # SMTP 서버 종료 
        self.connection.quit()
