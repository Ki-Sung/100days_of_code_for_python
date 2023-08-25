import os
import requests 
from dotenv import load_dotenv

# dotenv 로드 
load_dotenv(verbose=True)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

class FlightSearch:
    # IATA 코드 생성 메소드 
    def get_destination_code(self, city_name):
        # Test용으로 "TESTING"을 반환하여 sheety가 동작하는지 확인!
        code = "TESTING"
        return code 