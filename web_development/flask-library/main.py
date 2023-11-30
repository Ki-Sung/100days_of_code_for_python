import sqlite3
from flask import Flask, render_template, request, redirect, url_for

## 웹 서버 정의 
app = Flask(__name__)       # Flask 객체 선언

## book 정보 - Database 역할
all_books = []

## 데이터 베이스 정의 
# 데이터베이스 연결 - 만약 데이터 베이스가 존재하지 않으면 생성
db = sqlite3.connect("books-colleciton.db") 

# 데이터 베이스 제어를 위해 커서 생성
cursor = db.cursor()

# 테이블 생성: books - id: int(Primary key) / title: varhcar(250), not null / author: varhcar(250), not null / rating: float, not null
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# 데이터 추가 
# cursor.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'J. K. Rowling', 9.3)")
# cursor.execute("INSERT INTO books VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 4.7)")
# db.commit()

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

