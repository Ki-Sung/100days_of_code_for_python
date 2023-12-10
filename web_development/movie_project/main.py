import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from form import RateMovieForm, FindMovieForm

load_dotenv(verbose=True)

# 상수 설정 
MOVIE_DB_SEARCH_URL = os.getenv('MOVIE_DB_SEARCH_URL')           # TMDB 영화 검색 API Endpoint
MOVIE_DB_MOVIE_URL = os.getenv("MOVIE_DB_MOVIE_URL")             # TMDB 검색(TMDB 영화 ID)후 영화 정보 추출 API Endpoint 
MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')                 # TMDB API Key 

# Falsk 선언 
app = Flask(__name__)                                            # 플라스크 실행을 위해 객체 선언
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'    # CSRF 보호 기능을 위한 토큰울 위한 비밀키 생성 
Bootstrap(app)                                                   # 플라스크 부트스트랩 대입 

# DB 생성 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'     # sqlite DB URL 지정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             # 콘솔에서 SQLALCHEMY_TRACK_MODIFICATIONS과 관련된 사용 중지 경고 표시 X 
db = SQLAlchemy(app)                                             # DB 객체 선언

# 데이터 베이스 내 테이블 정의
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)                      # id(index) - 데이터 타입: int, 특징: primary key
    title = db.Column(db.String(250), unique=True, nullable=False)    # 영화 제목 - 데이터 타입: str(250자), 특징: unique 값, null 값 허용
    year = db.Column(db.Integer, nullable=False)                      # 영화 개봉 년도 - 데이터 타입: int, 특징: null 값 허용
    description = db.Column(db.String(500), nullable=False)           # 영화 설명 - 데이터 타입: str(500자), 특징: null 값 허용 
    rating = db.Column(db.Float, nullable=True)                       # 영화 평점 - 데이터 타입: float, 특징: not null
    ranking = db.Column(db.Integer, nullable=True)                    # 영화 랭킹(평점 기준) - 데이터 타입: int, 특징: not null
    review = db.Column(db.String(250), nullable=True)                 # 영화 리뷰 - 데이터 타입: str(250자), 특징: not null
    img_url = db.Column(db.String(250), nullable=False)               # 영화 포스터 이미지 URL - 데이터 타입: str(250자), 특징: null 값 허용

# DB 생성 - 테이블이 없을 시 생성 
db.create_all()

## 모든 라우터를 정의 
# Home Page - url 체계: http://127.0.0.1:5000/
@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()               # DB에 저장 된 데이터 모두 불러오기(평점 기준으로 랭킹을 오름차순으로 정렬)
    
    for i in range(len(all_movies)):                                    # 위에서 정렬한 데이터를 기준으로 loop 돌기 
        all_movies[i].ranking = len(all_movies) - i                     # 각각 영화 랭킹 매기기 - 가장 첫 번째로 정렬된 영화가 낮은 랭킹을 받음
        
    db.session.commit()                                                 # 변경사항 커밋
    return render_template("index.html", movies=all_movies)             # 불러온 데이터 페이지에 랜딩

# Edite Page - 평점과 리뷰 변경 페이지 - http://127.0.0.1:5000/edit
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()                                        # WTForm 인 RateMovieForm 클래스 선언 
    movie_id = request.args.get("id")                             # DB id 기준 데이터 조회 
    movie = Movie.query.get(movie_id)                             # id 기준 데이터 조회 
    
    # 데이터 조회 후 유효성 검사로 검증 - 만약 사용자가 입력한 양식 데이터가 유효한 경우 유효한 양식 제줄(한 마디로 DB에 수정 데이터 저장)
    if form.validate_on_submit():                          
        movie.rating = float(form.rating.data)                    # rating 필드에 입력된 값 추출 후 부동 소수점으로 변환
        movie.review = form.review.data                           # review 필드에 입력된 값 추출 후 movie 개체의 review 속성에 할당
        db.session.commit()                                       # 변경된 사항 DB에 커밋
        
        return redirect(url_for("home"))                          # 커밋 완료 후 Home Page로 리다이렉션
    
    return render_template("edit.html", movie=movie, form=form)   # 지정한 HTML template를 렌더링 및 클라이언트 요청에 대한 응답으로 반환 

# Delete 기능 - 선택한 영화 데이터 삭제 
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")                      # DB id 기준 데이터 조회 
    movie = Movie.query.get(movie_id)                      # id 기준 데이터 조회 
    db.session.delete(movie)                               # 조회된 데이터 삭제 
    db.session.commit()                                    # 삭제 완료 후 DB에 커밋
    
    return redirect(url_for("home"))                       # 삭제 버튼 클릭 후 홈으로 리다이렉팅

# Add 기능 - 영화 데이터 추가
@app.route("/add", methods=["GET", "POST"])
def add_movive(): 
    form = FindMovieForm()                                # 영화 제목 추가 양식 클래스 선언
    
    # 데이터 조회 후 유효성 검사로 검증 - 만약 사용자가 입력한 양식 데이터가 유효한 경우 유효한 양식 제줄(한 마디로 DB에 수정 데이터 저장)
    if form.validate_on_submit():
        movie_title = form.title.data                                  # 영화 타이틀 
        # TMDB API 호출 받기 
        response = requests.get(
                                MOVIE_DB_SEARCH_URL,                   # TMDB API Endpoint URL 설정
                                params={                              
                                        "api_key": MOVIE_DB_API_KEY,   # 파라미터 설정 - TMDB API Key 설정
                                        "query": movie_title           # 파라미터 설정 - 영화 제목 검색 설정
                                        }
                                )
        data = response.json()["results"]                              # 응답 받은 데이터 결과 Json으로 출력
        return render_template("select.html", options=data)            # 응답 받은 데이터 select.html 화면에 랜더링
    
    return render_template("add.html", form=form)                      # add.html에 템플릿 랜더링

# Movie 검색 기능 - 영화 데이터 추가를 위한 검색 기능
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")                               # 영화 API ID 검색 - 쿼리 매개변수에서 영화 APi ID를 가져옴 
    if movie_api_id:                                                    # 만약 영화 API ID가 있다면
        movie_api_url = f"{MOVIE_DB_MOVIE_URL}/{movie_api_id}"          # Movie 서칭 엔드포인트와 찾고자 하는 영화 ID로 API URL 지정
        # TMDB API 호출 받기 
        response = requests.get(                                        
                                movie_api_url,                          # TMDB API Endpoint URL 설정 - 영화 서치 API 
                                params={"api_key": MOVIE_DB_API_KEY,    # 파라미터 설정 - TMDB API Key 설정
                                        "language": "ko"}               # 파라미터 설정 - 언어 설정
                                )    
        data = response.json()                                          # 응답 받은 데이터 결과 Json으로 출력
        # 응답 받은 데이터 기준으로 DB에 넣어야할 데이터 설정 
        new_movie = Movie(
            title = data["title"],                                                      # 영화 제복 
            year = data["release_date"].split("-")[0],                                  # 영화 개봉 년도 
            img_url = "https://www.themoviedb.org/t/p/w1280" + data["poster_path"],     # 포스터 URL 
            description = data["overview"]                                              # 영화 설명 (줄거리 설명)
        )
        db.session.add(new_movie)                                                       # 조회된 데이터 추가 
        db.session.commit()                                                             # 수정사항 커밋 
        
        return redirect(url_for("rate_movie", id=new_movie.id))                         # 저장 후 Home 페이지로 리다이렉팅

# 앱 실행 - 실행시 디버그 모드 On
if __name__ == '__main__':
    app.run(debug=True)
