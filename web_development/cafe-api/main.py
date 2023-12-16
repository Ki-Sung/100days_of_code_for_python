from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

## 데이터 베이스 연결 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## Cafe 테이블 구성
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # mothod 정의 - cafe 객체를 딕셔너리로 변환하는 역할 (이렇게 하면 딕셔너리로 반환하여 JSON 형태로 반환하는 작업이 용이해짐)
    def to_dict(self):
        # 방법 1
        dictionary = {}                                             # 저장을 위한 빈 딕셔너리 생성 
        for column in self.__table__.columns:                       # 테이블의 모든 column에 대한 정보를 가져와 loop 진행
            dictionary[column.name] = getattr(self, column.name)    # 현재 객체에서의 column 값을 가져오기 
        return dictionary                                           # 저장된 딕셔너리 반환

        # 방법2 - 딕셔너리 구성하여 반환 
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
## 모든 라우터 정의 
# home page - url 체계: http://127.0.0.1:5000/
@app.route("/")
def home():
    # 지정한 url 체계로 index.html 템플릿 랜더링
    return render_template("index.html")

# HTTP GET - Read Record 
# random하게 카페 정보 조회 Page - url 체계: http://127.0.0.1:5000/random
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()                            # SQLAlchemy를 사용하여 Cafe 모델에 대한 쿼리 개체 생성 후 모든 레코드 검색
    random_cafe = random.choice(cafes)                              # random.choice 함수를 사용하여 모든 카페 목록에서 임의로 카페 선택 
    return jsonify(cafe=random_cafe.to_dict())                      # 랜덤으로 선택된 카페 json 형식으로 변환 

# 모든 카페 정보 조회 page - url 체계: http://127.0.0.1:5000/all
@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()                            # SQLAlchemy를 사용하여 Cafe 모델에 대한 쿼리 개체 생성 후 모든 레코드 검색
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])        # 모든 카페 json 형식으로 변환

# 위치 매개변수를 기반으로 카페를 검색하는 page - url 체계: http://127.0.0.1:5000/search?loc={cafe name}
@app.route("/search")
def search_cafes():
    query_location = request.args.get("loc")                                     # 사용자가 입력한 검색어를 query_location 변수에 저장
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()     # DB에서 사용자가 입력한 위치와 일치한느 카페를 조회 
    
    # 조회된 카페가 있는지 확인 
    if cafe:
        return jsonify(cafe=cafe.to_dict())                                       # 만약 조회된 카페가 있다면 해당 카페의 정보를 JSON 형식으로 응답 
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})   # 만약 없다면 해당 위치에 카페가 없다는 에러 메시지를 JSON 형식으로 응답

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
