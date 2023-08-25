from datetime import datetime, timedelta
from flight_modules.data_manager import DataManager
from flight_modules.flight_search import FlightSearch

data_manager = DataManager()                      # 클래스 객체 생성 
sheet_data = data_manager.get_destination_data()  # 시트 데이터를 불러오기 위해 생성한 객체에 get_destination_data 메소드 호출
flight_search = FlightSearch()                    # FlightSearch 클래스 객체 선언 (Flight Search API를 사용을 위한)

# 출발지 설정 
ORIGIN_CITY_IATA = "ICN"

if sheet_data[0]["iataCode"] == "":        # sheet_data에 "iataCode"의 키값이 없는 경우 
    for row in sheet_data:                 
        row["iataCode"] = flight_search.get_destination_code(row["city"]) # sheet_data의 각 도시 이름을 하나씩 전달 
    # 6. IATA CODE를 고치기 위해 update_destination_codes 메소드 사용
    data_manager.destination_data = sheet_data       # 수정할 Sheet 데이터 불러오기 
    data_manager.update_destination_codes()          # IATA 코드 수정 하기
    
tomorrow = datetime.now() + timedelta(days=1)                      # 기준 날짜 - 내일 날짜 
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))   # 최대 날짜 - 6개월 날짜 

for destination in sheet_data:
    flight = flight_search.check_flights(                          # 항공권 검색 (구글 시트 안에 있는 원하는 목적지 기준으로 추출)
        ORIGIN_CITY_IATA,                                          # 출발지 
        destination["iataCode"],                                   # 도착지(구글 시트 안에 있는 데이터 기준 )
        from_time=tomorrow,                                        # 출발 날짜 
        to_time=six_month_from_today                               # 돌아오는 날짜 
    )

