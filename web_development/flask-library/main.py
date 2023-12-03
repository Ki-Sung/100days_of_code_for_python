from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

## 웹 서버 및 DB 정의 
app = Flask(__name__)       # Flask 객체 선언
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'   # sqlite DB Url 지정
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                          # 콘솔에서 SQLALCHEMY_TRACK_MODIFICATIONS과 관련된 사용 중지 경고 표시 X 
db = SQLAlchemy(app)                                                          # DB 객체 선언 

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
db.create_all()                                                             # 지정된 DB생성 
    
## CRUD
# Create - 데이터 추가
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# Read - 데이터 전체 읽기
# all_books = db.session.query(Book).all()

# Read - 특정 데이터 읽기
# book = Book.query.filter_by(title="Harry Potter").first()

# Update - 쿼리별 데이터 업데이트하기
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# Update - 기본키로 데이터 업데이트 하기
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# Delete - 기본키로 특정 데이터 삭제 
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


## 모든 라우터를 정의
# Home Page - url 체계: http://127.0.0.1:5000/
@app.route('/')
def home():
    # books = Book.query.all()
    books = db.session.query(Book).all()                # DB에 저장 된 데이터 모두 불러오기 
    return render_template("index.html", books=books)   # 불러온 데이터 페이지에 랜딩

# Add book Page - url 체계 - http://127.0.0.1:5000/add
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":                      # 만약 메소드가 POST일 경우 
        # 새로운 book 데이터 생성 
        new_book = Book(
            title=request.form["title"],              # 도서 제목
            author=request.form["author"],            # 도서 작가 
            rating=request.form["rating"]             # 도서 평점
        ) 
        # 데이터 베이스에 추가
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for("home"))              # 저장 후 Home으로 리다이렉션
        
    return render_template("add.html")                # add.html 랜딩

# Edit Rate Page - url 체계: http://127.0.0.1:5000/eidit?id=1
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":                         # 만약 메소드가 POST일 경우 
        # 데이터 베이스에 변동 사항  업데이터
        book_id = request.form["id"]                     # 쿼리로 book id 지정
        book_to_update = Book.query.get(book_id)         # 지정된 book id 기준 데이터 불러오기 
        book_to_update.rating = request.form["rating"]   # book id 기준으로 불러온 데이터 중 평점 데이터 수정
        db.session.commit()                              # 변동사항 커밋 
        return redirect(url_for("home"))                 # 변동 버튼 클릭 후 홈으로 리다이렉팅
    
    # 요청 메소드가 GET일 경우 실행
    book_id = request.args.get("id")                         # 쿼리 매개변수에서 id 값을 가져옴
    book_selected = Book.query.get(book_id)                  # 가져온 id를 사용하여 DB에 해당하는 도서 가져오기
    return render_template("edit.html", book=book_selected)  # 가져온 도서 정보를 사용하여 edit.html 템플릿을 랜더링 하고 해당 템플릿에 book 변수로 전달

# # Delete book list 
@app.route("/delete")
def delete():
    book_id = request.args.get("id")                    # 쿼리로 book id 지정
        
    # book_id 기준 데이터 삭제하기 
    book_to_delete = Book.query.get(book_id)            # 지정된 book id 기준 데이터 불러오기 
    db.session.delete(book_to_delete)                   # 데이터 삭제
    db.session.commit()                                 # 변동사항 커밋
    
    return redirect(url_for("home"))                    # 삭제 버튼 클릭 후 홈으로 리다이렉팅

if __name__ == "__main__":
    app.run(debug=True)

