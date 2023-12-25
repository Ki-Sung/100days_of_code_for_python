from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
from form import AddCafeForm

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

# HTTP POST - Create Record
# 새로운 카페 추가 - url 체계: http://127.0.0.1:5000/add
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(                                              # Cafe 모델을 이용하여 새로운 카페 데이터 생성 
        name=request.form.get("name"),                              # "name"의 키 값을 가져와 "new_cafe"의 "name" 필드에 설정 
        map_url=request.form.get("map_url"),                        # "map_url"의 키 값을 가져와 "new_cafe"의 "map_url" 필드에 설정 
        img_url=request.form.get("img_url"),                        # "img_url"의 키 값을 가져와 "new_cafe"의 "img_url" 필드에 설정 
        location=request.form.get("loc"),                           # POST 요청으로 전달된 "loc" 키 값을 가져와 "new_cafe"의 "location" 필드에 설정 
        has_sockets=bool(request.form.get("sockets")),              # POST 요청으로 전달된 "sockets" 키의 값을 가져와서 new_cafe의 "has_sockets" 필드에 설정
        has_toilet=bool(request.form.get("toilet")),                # POST 요청으로 전달된 "toilet" 키의 값을 가져와서 new_cafe의 "has_toilet" 필드에 설정
        has_wifi=bool(request.form.get("wifi")),                    # POST 요청으로 전달된 "wifi" 키의 값을 가져와서 new_cafe의 "has_wifi" 필드에 설정
        can_take_calls=bool(request.form.get("calls")),             # POST 요청으로 전달된 "calls" 키의 값을 가져와서 new_cafe의 "can_take_calls" 필드에 설정
        seats=request.form.get("seats"),                            # POST 요청으로 전달된 "seats" 키의 값을 가져와서 new_cafe의 "seats" 필드에 설정
        coffee_price=request.form.get("coffee_price"),              # POST 요청으로 전달된 "coffee_price" 키의 값을 가져와서 new_cafe의 "coffee_price" 필드에 설정
    )
    db.session.add(new_cafe)                                                    # SQLAlchemy의 세션에 새로운 카페 데이터 추가
    db.session.commit()                                                         # 변동 사항 DB에 커밋
    return jsonify(response={"success": "Successfully added the new cafe."})    # JSON 형식의 응답을 반환 - 만약 성공시 지정한 메시지를 출력 

# HTTP PUT/PATCH - Update Record
# 카페 id 기준으로 데이터를 불러온 뒤 커피 가격 업데이트 - url 체계: http://127.0.0.1:5000/update-price/<int:cafe_id>
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")                                           # PATCH 요청의 쿼리 문자열에서 "new_price" 키 값을 가져와 "new_price" 변수에 할당 
    cafe = db.session.query(Cafe).get(cafe_id)                                          # "cafe_id"에 해당하는 카페를 DB에서 조회 
    if cafe:                                                                            # 조회된 카페가 존재할 경우 
        cafe.coffee_price = new_price                                                       # 조회된 카페의 "coffe_price" 필드를 새로운 가격인 "new_price"로 업데이트 
        db.session.commit()                                                                 # 변동사항 DB에 커밋
        return jsonify(response={"success": "Successfully updated the cafe price."})        # JSON 형식의 응답을 반환 - 만약 성공시 지정한 메시지를 출력 
    else:                                                                               # 조회된 카페가 없을 경우
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})     # JSON 형식의 응답을 반환 - 에러 응답 메시지를 출력 

## HTTP DELETE - Delete Record
# 카페 id 기준으로 데이터를 불러온 뒤 해당 카페 정보 모두 삭제 - url 체계: http://127.0.0.1:5000/report-closed/<int:cafe_id>
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")                                               # DELETE 요청의 쿼리 문자열에서 "api-key" 키의 값을 가져와서 api_key 변수에 할당
    if api_key == "TopSecretAPIKey":                                                    # 가져온 api_key가 "TopSecretAPIKey"와 같은 경우
        cafe = db.session.query(Cafe).get(cafe_id)                                      # cafe_id에 해당하는 카페를 데이터베이스에서 조회
        if cafe:                                                                                                    # 조회된 카페가 존재하는 경우 
            db.session.delete(cafe)                                                                                 # 조회된 카페를 DB에서 삭제 
            db.session.commit()                                                                                     # 변경 사항 DB에 커밋 
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200           # JSON 형식의 응답을 반환 - 만약 성공시 지정한 메시지를 출력 
        else:                                                                                                       # 조회된 카페가 없는 경우  
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404    # 에러 내용 JSON 형식으로 응답 변환 - 404 에러도 함꼐 응답 
    else:                                                                                                               # api_key가 "TopSecretAPIKey"가 아닌 경우 
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403  # 에러 내용 JSON 형식으로 응답 변환 - 403 에러도 함꼐 응답 

if __name__ == '__main__':
    app.run(debug=True)
