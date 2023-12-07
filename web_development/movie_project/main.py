import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from form import RateMovieForm, FindMovieForm

from form import RateMovieForm

load_dotenv(verbose=True)

MOVIE_DB_SEARCH_URL = os.getenv('MOVIE_DB_SEARCH_URL')
MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY')

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
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# 더미 데이터 - 실행하고 주석 처리하기 
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://www.themoviedb.org/t/p/original/t4w6KSB5Zhfo6MFNlYjKT0L2Pno.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

## 모든 라우터를 정의 
# Home Page - url 체계: http://127.0.0.1:5000/
@app.route("/")
def home():
    movies = db.session.query(Movie).all()                # DB에 저장 된 데이터 모두 불러오기 
    return render_template("index.html", movies=movies)   # 불러온 데이터 페이지에 랜딩

# Edite Page - 평점과 리뷰 변경 페이지 - http://127.0.0.1:5000/edit
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()                                 # WTForm 인 RateMovieForm 클래스 선언 
    movie_id = request.args.get("id")                      # DB id 기준 데이터 조회 
    movie = Movie.query.get(movie_id)                      # id 기준 데이터 조회 
    
    # 데이터 조회 후 유효성 검사로 검증 - 만약 사용자가 입력한 양식 데이터가 유효한 경우 유효한 양식 제줄(한 마디로 DB에 수정 데이터 저장)
    if form.validate_on_submit():                          
        movie.rating = float(form.rating.data)             # rating 필드에 입력된 값 추출 후 부동 소수점으로 변환
        movie.review = form.review.data                    # review 필드에 입력된 값 추출 후 movie 개체의 review 속성에 할당
        db.session.commit()                                # 변경된 사항 DB에 커밋
        
        return redirect(url_for("home"))                   # 커밋 완료 후 Home Page로 리다이렉션
    
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
        movie_title = form.title.data                     # 영화 타이틀 
        # TMDB API 호출 받기 
        response = requests.get(
                                MOVIE_DB_SEARCH_URL,                   # TMDB API Endpoint URL 설정
                                params={                              
                                        "api_key": MOVIE_DB_API_KEY,   # 파라미터 설정 - TMDB API Key 설정
                                        "query": movie_title           # 파라미터 설정 - 영화 제목 검색 설정
                                        }
                                )
        data = response.json()["results"]                              # 응답 받은 데이터 Json으로 출력
        return render_template("select.html", options=data)            # 응답 받은 데이터 select.html 화면에 랜더링
    
    return render_template("add.html", form=form)                      # add.html에 템플릿 랜더링


if __name__ == '__main__':
    app.run(debug=True)
