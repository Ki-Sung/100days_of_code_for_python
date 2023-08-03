# Trivia Database API를 이용해서 데이터 불러오기 

# 모듈 불러오기 
import requests

# 파라미터 설정 
prameters = {
    "amount": 20,
    "type": "boolean",
    # "categofy": number(int)
}

response = requests.get("https://opentdb.com/api.php", params=prameters)   # 앤드포인트로 요청 받기 
response.raise_for_status()                                                # 응답코드 - 200이 아니면 예외를 발생 시킴 

question_data = response.json()["results"]                                  # Trivia API에서 가져온 데이터 저장
