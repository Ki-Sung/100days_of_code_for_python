import os
import requests
from dotenv import load_dotenv

import smtplib
from email.mime.text import MIMEText     # email 모듈 중 메시지 제목과 본문을 설정하기 위한 라이브러리
from email.mime.multipart import MIMEMultipart  # email 모듈 메일의 데이터 영역의 메시지를 만드는 라이브러리

# dotenv 로드 
load_dotenv(verbose=True)

# Stock info - Tesla
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Endpoint
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# solution 2

import requests 

STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_API")
NEWS_API_KEY = os.getenv("NEWS_API")

# Parameters 
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# 데이터 호출 및 응답 
response = requests.get(STOCK_ENDPOINT, params=stock_params)   # 앤드포인트로 요청 받기
response.raise_for_status()                                    #응답 코드 - 200이 아니면 예외를 발생 시킴  

data = response.json()["Time Series (Daily)"]                  # 200을 받으면 데이터 JSON 형식으로 받기

# 필요한 데이터 불러오기 
data_list = [value for (key, value) in data.items()]           # data_list 불러오기 

# 어제자 종가 데이터 불러오기 
yesterday_data = data_list[0]                                  # 어제자 데이터 불러오기 
yesterday_close_price = yesterday_data["4. close"]             # 어제자 종가 데이터 불러오기 
print(yesterday_close_price)

# 그제 종가 데이터 불러오기
day_before_yesterday_data = data_list[1]                                   # 그제자 데이터 불러오기 
day_before_yesterday_colse_price = day_before_yesterday_data["4. close"]   # 그제자 종가 데이터 불러오기 
print(day_before_yesterday_colse_price)

# 어제 폐장가와 엊그제 폐장가 비율 구하기 
difference = abs(float(yesterday_close_price) - float(day_before_yesterday_colse_price))  # 어제 폐장가, 엊그제 폐장가 차이 구하기 (절대값으로)
diff_percent = (difference / float(yesterday_close_price)) * 100                          # 퍼센트 비율 구하기 

## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# 만약 페장가 비율이 4 퍼센트를 초과할 경우 get new 출력 
if diff_percent > 1:
    # news_api_parameters
    new_parameters = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=new_parameters)    # 앤드포인트로 요청 받기
    news_response.raise_for_status()                                      # 응답 코드 - 200이 아니면 예외를 발생 시킴 
    article = news_response.json()["articles"]                            # 기사 데이터 응답 받기 
    
    three_articles = article[:3]                                          # 최신 기사 3개 불러오기 
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

