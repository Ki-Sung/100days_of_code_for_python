import os
import requests      
from datetime import datetime
from dotenv import load_dotenv

# dotenv 로드 
load_dotenv(verbose=True)

# 파라미터에 들어갈 상수 값들 
GENDER = os.getenv("GENDER")          # 성별 
WEIGHT_KG = os.getenv("WEIGHT_KG")    # 몸무게 
HEIGHT_CM = os.getenv("HEIGHT_CM")    # 키 
AGE = os.getenv("AGE")                # 나이 

# USER 및 API 정보 
APP_ID = os.getenv("NUTRITIONIX_APP_ID")        # 뉴트리셔닉스 App ID 
API_KEY = os.getenv("NUTRITIONIX_API_KEY")      # 뉴트리셔닉스 API Key 

# 엔드 포인트 설정 
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"  # nutritionix endpoint
SHEETY_ENDPOINT = "https://api.sheety.co/52479a109dad9a29f7d2ae8bbb70d1a7/myWorkouts/workouts"  # sheety endpoint 

# 시간 설정 
now = datetime.now()                   # datetime 객체 선언 - 현재 시간으로 
today_date = now.strftime("%Y/%m/%d")  # 날짜 설정 
today_time = now.strftime("%X")        # 시간 설정 

exercise_text = input("Tell me which exercise you did: ")     # 오늘 운동 뭐했는지 입력 후 저장 - 파라미터 쿼리 값 

# 인증을 위해 해더 값 입력 
headers = {
    "x-app-id": APP_ID,      # 뉴트리셔닉스 App ID
    "x-app-key": API_KEY,    # 뉴트리셔닉스 API Key 
}

# 파라미터 값 입력 
parameters = {
    "query": exercise_text,       # 쿼리 
    "gender": GENDER,             # 성별  
    "weight_kg": WEIGHT_KG,       # 몸무게 
    "height_cm": HEIGHT_CM,       # 키 
    "age": AGE                    # 나이
}

# 데이터 불러오기 
response = requests.post(url=END_POINT, json=parameters, headers=headers)   # Post 방식으로 데이터 불러오기 
result = response.json()              # Post 방식으로 불러온 데이터 JSON 형태로 반환                       

# 추출한 데이터 구글시트에 저장 
for exercise in result["exercises"]:  
    sheet_input = {
        "workout": {                   # 위에 입력한 workout 데이터 
            "date": today_date,        # 금일 날짜 
            "time": today_time,        # 업로드 시간
            "exercise": exercise["name"].title(),   # 운동명 
            "duration": exercise["duration_min"],   # 지속 시간 
            "calories": exercise["nf_calories"]     # 운동 칼로리
        }
    }
    
    # 데이터 입력을 위해 POST 방식으로 입력 
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input)
    
    # 결과 추출
    print(sheet_response.text)