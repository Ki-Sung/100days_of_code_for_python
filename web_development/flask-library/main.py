import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

## 웹 서버 및 DB 정의 
app = Flask(__name__)       # Flask 객체 선언
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'   # sqlite DB Url 지정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                          # 콘솔에서 SQLALCHEMY_TRACK_MODIFICATIONS과 관련된 사용 중지 경고 표시 X 
db = SQLAlchemy(app)                                                          # DB 객체 선언 

## book 정보 - Database 역할
all_books = []

## 데이터 베이스 정의 - SQLite3
# 데이터베이스 연결 - 만약 데이터 베이스가 존재하지 않으면 생성
# db = sqlite3.connect("books-colleciton.db") 

# 데이터 베이스 제어를 위해 커서 생성
# cursor = db.cursor()

# 테이블 생성: books - id: int(Primary key) / title: varhcar(250), not null / author: varhcar(250), not null / rating: float, not null
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# 데이터 추가 
# cursor.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'J. K. Rowling', 9.3)")
# cursor.execute("INSERT INTO books VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 4.7)")
# db.commit()

## 데이터 베이스 정의 - SQLAlchemy
# Book 모델 정의 - Book Table 생성
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)                       # 컬럼 설정 - id: 고유 index 번호 (프라미어리 키)
    title = db.Column(db.String(250), unique=True, nullable=False)     # 컬럼 설정 - title: 가변 길이 문자열 최대 길이 250자, 중복 허용 X, Null 값 허용 X
    author = db.Column(db.String(250), nullable=False)                 # 컬럼 설정 - author: 가변 길이 문자열 최대 길이 250자, Null 값 허용 X
    rating = db.Column(db.Float, nullable=False)                       # 컬럼 설정 - rating: float, Null 값 허용 X

# 만약 데이터 베이스가 없다면 생성
with app.app_context():
    db.create_all()                                                             # 지정된 DB생성 
    
    # 데이터 추가 
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

## 모든 라우터를 정의
# Home Page - url 체계: http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template("index.html", all_books=all_books)

# Add book Page - url 체계 - http://127.0.0.1:5000/add
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":                      # 만약 메소드가 POST일 경우 
        # 새로운 book 데이터 저장
        new_book = {
            "title": request.form["title"],           # book 제목 
            "author": request.form["author"],         # 작가명
            "rating": request.form["rating"]          # book 평가 
        }
        all_books.append(new_book)                    # 입력한 데이터 all_books에 저장
        
        return redirect(url_for("home"))              # 저장 후 Home으로 리다이렉션
        
    return render_template("add.html")                # add.html 랜딩


if __name__ == "__main__":
    app.run(debug=True)

