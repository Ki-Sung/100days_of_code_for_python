import os
import requests
from dotenv import load_dotenv

# dotenv 로드 
load_dotenv(verbose=True)

# sheety API END Point 
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")

# Sheety API를 이용하여 구글시트에 있는 데이터를 조회, 업데이트 하는 클래스 
class DataManager:
    # 클래스 내 초기화 매소드 설정 
    def __init__(self):
        self.destination_data = {}   # json 데이터를 담가 위해 초기에 설정함 
    
    # google sheet에 데이터를 불러오기 위한 메소드
    def get_destination_data(self):
        # 1. Sheety API를 사용해서 google sheet에 있는 데이터 get 방식으로 가져오기 
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)     # 엔드포인트 기준 get 방식으로 데이터 받기 
        data = response.json()                                  # 요청 받은 데이터를 Json 방식으로 데이터 저장
        self.destination_data = data["prices"]                  # 데이터에 prices 키 값안에 있는 데이터 받아오기 
        # 2. 로그에 출력할 JSON 데이터를 이쁘게 보여줄 pprint 사용 
        # pprint(data)
        return self.destination_data                            # destination_data 반환(get_destination_data 메소드가 호출되면 리턴해줌))
    
    # 5. PUT요청을 위한 update_destination_codes 메소드 만들기
    # PUT 방식으로 데이터를 업데이트 하기 위한 메소드 
    def update_destination_codes(self):
        for city in self.destination_data:                      
            new_data = {                                        # get 방식으로 받은 데이터에서 city IATA CODE를 저장 
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            
            response = requests.put(                           # 데이터를 수정하기 위해 PUT 방식으로 호출 
            url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",      # end point url 설정 
            json=new_data                                      # 수정할 데이터 지정 
            )
            print(response.text)                               # 결과 출력 