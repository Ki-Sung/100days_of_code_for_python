import os
import requests 
from flight_modules.flight_data import FlightData
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
    
    # 항공편 체크를 위한 메소드 
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # header 설정 - API Key 
        headers = {
            "apikey": TEQUILA_API_KEY
            }
        
        # 파라미터 설정 
        params = {
            "fly_from": origin_city_code,                 # 출발지 코드 (IATA 코드로 표현)
            "fly_to": destination_city_code,              # 도착지 코드 (IATA 코드로 표현)
            "date_from": from_time.strftime("%d/%m/%Y"),  # 출발 날짜 (dd/mm/yy 형식)
            "date_to": to_time.strftime("%d/%m/%Y"),      # 돌아오는 날짜 (dd/mm/yy 형식)
            "nights_in_dst_from": 7,                      # 최소 체류 기간(일)
            "nights_in_dst_to": 28,                       # 최대 체류 기간(일)
            "one_for_city": 1,                            # 매개 변수에서 포함된 가장 저렴한 항공편 반환
            "max_stopovers": 0,                           # 전체일정(출국+귀국)당 최대 체류 횟수, 직항편을 원하는 경우 0으로 설정
            "curr": "KRW"                                 # 가격 화폐단위 한국 원 
        }
        
        response = requests.get(                          # 데이터 요청 받기 
            url=f"{TEQUILA_ENDPOINT}/v2/search",          # Endpoint 설정 
            headers=headers,                              # header 설정 
            params=params                                 # 파라미터 설정 
        )
        
        try:                                      
            data = response.json()["data"][0]             # 설정한 Endpoint, header, 파라미터로 데이터 받기 
        except IndexError:                                # 예외적으로 에러가 발생하면(IndexError)
            print(f"No Flights found for {destination_city_code}.")   # 해당 코드는 찾을 수 없다라는 에러 출력 
            return None 
        
        flight_data = FlightData(                                          # 데이터를 호출 받으면 키값 별로 데이터 저장 
            price=data["price"],                                           # 항공편 가격
            origin_city=data["route"][0]["cityFrom"],                      # 출발할 도시 
            origin_airport=data["route"][0]["flyFrom"],                    # 출발할 공항
            destination_city=data["route"][0]["cityTo"],                   # 도착할 도시 
            destination_airport=data["route"][0]["flyTo"],                 # 도착할 공항 
            out_date=data["route"][0]["local_departure"].split("T")[0],    # 출발 날짜    
            return_date=data["route"][1]["local_departure"].split("T")[0]  # 돌아올 날짜
        )
        print(f"{flight_data.destination_city}: ₩{flight_data.price}")     # 결과 출력
        return flight_data