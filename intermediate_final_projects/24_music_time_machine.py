import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm
from dotenv import load_dotenv
import requests 
from bs4 import BeautifulSoup

# dotenv 로드 
load_dotenv(verbose=True)

# spotify info
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")     # 스포티파이 클라이언트 ID 
SPOTIFY_SECRET_KEY = os.getenv("SPOTIFY_SECRET_KEY")   # 스포티파이 시크릿키

# spotify 인증
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read playlist-modify-public",  # 비공개 플레이 리스트 만들기 
        redirect_uri="http://example.com",                 # 리다이렉션 URI
        client_id=SPOTIFY_CLIENT_ID,                       # 스포티파이 클라이언트 아이디 
        client_secret=SPOTIFY_SECRET_KEY,                  # 스포티파이 클라이언트 시크릿키 
        show_dialog=True,                                  # 다이어로그 여부 
        cache_path="./data/token.txt"                      # 인증 후 저장할 캐시 경로
    )
)

# 클라이언트 id 확인 및 프로프트 입력 
user_id = sp.current_user()["id"]     # 스포티파이 인증 ID 확인
question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")    # 원하는 날짜 입력 

# 내가 원하는 날짜를 기준으로 빌보드 Hot 100에 있는 제목 스크래핑 하기 
url = f"https://www.billboard.com/charts/hot-100/{question}/"                                         # 스크래핑 대상 url
response = requests.get(url)                                                                          # 지정한 url로 요청받기
bilboard_page = response.text                                                                         # 페이지 정보 받기 

soup = BeautifulSoup(bilboard_page, "html.parser")                                                    # html 파싱 하기 
music_title_spans = soup.select("li > ul > li > h3")                                                  # 빌보드 노래 타이틀 태그 추출 
music_title = [title.getText().replace("\n", "").replace("\t", "") for title in music_title_spans]    # 타이틀 태그 기준 타이틀만 받아온 후 저장

# 스크래핑한 제목을 바탕으로 스포티파이 내 검색 후 uri 리스트 만들기 
song_uris = []                                                                     # 결과를 저장하기 위한 빈 리스트 
year = question.split("-")[0]                                                      # 년도만 추출 
for music in tqdm(music_title):
    result = sp.search(q=f"track:{music} year:{year}", type="track")               # 해당 노래 타이틀 기준 uri 검색(쿼리=track:노래 타이틀, year:년도, type=track)
    
    # 만약 검색할 음악이 없을 경우 예외처리 
    try:
        uri = result["tracks"]["items"][0]["uri"]                                   # uri 추출 
        song_uris.append(uri)                                                       # 결과 저장을 위한 빈 리스트에 저장
    except IndexError:                                                              # 만약 IndexError가 추출될 경우 
        print(f"{music} doesn't exist in Spotify. Skipped.")                         # 해당 음악은 검색이 없으므로 스킵하겠다라고 출력 후 예외처리


