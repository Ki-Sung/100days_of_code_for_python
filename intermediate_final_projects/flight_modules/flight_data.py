# 항공권 데이터를 위한 FlightData 클래스 
class FlightData:
    # 초기값 설정 
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price                              # 항공권 가격 
        self.origin_city = origin_city                  # 출발 도시 
        self.origin_airport = origin_airport            # 출발 공항 
        self.destination_city = destination_city        # 목적지 도시 
        self.destination_airport = destination_airport  # 목적지 공항 
        self.out_date = out_date                        # 출발 날짜 
        self.return_date = return_date                  # 돌아오는 날짜