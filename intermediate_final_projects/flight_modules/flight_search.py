import os
import requests 
from dotenv import load_dotenv

# dotenv 로드 
load_dotenv(verbose=True)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

# 7. IATA 코드 출력을 위한 메소드 기능 구현 
class FlightSearch:
    # IATA 코드 생성 메소드 
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"   # endpoint 설정
        
        # header 설정 - API Key 
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        
        # 파라미터 설정 
        params = {
            "term": city_name,                      # 쿼리 -> 도시명(영어로)
            "location_types": "city"                # location 타입 설정 -> 도시명
        }
        
        # header, 파라미터를 기준으로 데이터 호출 
        response = requests.get(
            url=location_endpoint,                  # 엔드포인트 
            headers=headers,                        # 헤더 
            params=params                           # 파라미터
        )
        
        result = response.json()["locations"]       # 응답 받은 데이터 중 location 키값 호출 
        code = result[0]["code"]                    # 저장한 result 데이터 중 첫 번째 코드 키값 호출 
        
        return code 