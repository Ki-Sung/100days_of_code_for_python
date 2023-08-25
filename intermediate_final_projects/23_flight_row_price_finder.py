import requests
from flight_modules.data_manager import DataManager
from flight_modules.flight_search import FlightSearch

data_manager = DataManager()                      # 클래스 객체 생성 
sheet_data = data_manager.get_destination_data()  # 시트 데이터를 불러오기 위해 생성한 객체에 get_destination_data 메소드 호출
# pprint(sheet_data)

if sheet_data[0]["iataCode"] == "":        # sheet_data에 "iataCode"의 키값이 없는 경우 
    flight_search = FlightSearch()         # FlightSearch 클래스 객체 선언 (Flight Search API를 사용을 위한)
    for row in sheet_data:                 
        row["iataCode"] = flight_search.get_destination_code(row["city"]) # sheet_data의 각 도시 이름을 하나씩 전달 
    print(sheet_data)
    
    # 6. IATA CODE를 고치기 위해 update_destination_codes 메소드 사용
    data_manager.destination_data = sheet_data       # 수정할 Sheet 데이터 불러오기 
    data_manager.update_destination_codes()          # IATA 코드 수정 하기

