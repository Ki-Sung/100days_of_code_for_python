import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# dotenv 로드 
load_dotenv(verbose=True)


GRAPH_ID = "graph1"                             # 그래프 ID
USER_NAME = os.getenv("PIXELA_USER_NAME")       # pixela 유저 이름
TOKEN = os.getenv("PIXELA_TOKEN")               # pixela 토큰 
TODAY = datetime.now().strftime("%Y%m%d")       # 오늘날짜 생성 
# YESTERDAY = datetime(year=2023, month=8, day=14).strftime("%Y%m%d")  # 어제 날짜 설정

pixel_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"

# 그래프 생성을 위해 요청할 key 값들 설정 
pixel_config = {
    "date": TODAY,            # 날짜(string) - yyyymmdd 형식 
    "quantity": input("How many kilomters did you runnig today? "),   # 픽셀 개수(string) - int, float 형식 
}

# 헤더 값 설정
headers = {
    "X-USER-TOKEN": TOKEN          # X-USER-TOKEN 설정 
}

# 지정한 키값들로 데이터(그래프)요청 받기 - POST 방식으로 
response = requests.post( 
                          url=pixel_endpoint,  # 엔드포인트 URL 
                          json=pixel_config,   # 그래프 생성을 위한 설정 값들 
                          headers=headers      # header 값 설정 
                        )

print(response.text)        # 요청 후 결과 메시지 출력