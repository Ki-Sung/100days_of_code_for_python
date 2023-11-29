from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from form import CafeForm
import csv

# 웹 서버 정의 

app = Flask(__name__)                                           # Flask 객체 선언
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'   # 애플리케이션 비밀키 설정 - 비밀 키는 세션 및 CSRF(Cross-Site Request Forgery) 보호 및 Flask 기능을 보호하는데 사용
Bootstrap(app)                                                  # Flask 앱의 Bootstrap을 초기화 

## 모든 라우터를 정의 

# Home Page - url 체계: http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("index.html") 

# Add Cafe Page - url 체계 - http://127.0.0.1:5000/add
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()                                           # CafeForm 객체 선언 
    if request.method == 'POST' and form.validate_on_submit():  # 만약 메소드가 POST, 양식이 성공적으로 검증된다면
        # 새로운 카페 데이터 form - list 형식 (add form에 데이터를 입력한 데이터를 받음)
        new_cafe_data = [
            form.cafe.data,                   # cafe 이름
            form.location.data,               # cafe 위치  
            form.open_time.data,              # cafe 오픈 시간
            form.close_time.data,             # cafe 클로즈 시간
            form.coffee_rating.data,          # cafe 커피 등급
            form.wifi_rating.data,            # cafe 와이파이 등급
            form.power_rating.data            # cafe 전력 등급 
        ]
        
        # csv 파일에 데이터 처리
        with open('cafe-data.csv', mode='a', newline='') as csv_file:   # cafe-data.csv에 append 모드로 열기  
            csv_writer = csv.writer(csv_file)                           # csv writer로 csv 파일 준비
            csv_writer.writerow(new_cafe_data)                          # 새로운 카페 데이터를 csv파일에 쓰기 
            
        return redirect(url_for('cafes'))                               # csv 파일에 저장 후 'cafes'경로로 리다이렉션
    
    # csv 파일 읽기 
    with open('cafe-data.csv', newline='') as csv_file:                 # cafe-data.csv를 읽기 모드로 열기 
        csv_data = csv.reader(csv_file, delimiter=',')                  # csv reader로 csv 파일 읽기 
        list_of_rows = [row for row in csv_data]                        # 읽은 csv 리스트로 정렬 

    return render_template('add.html', form=form, cafes=list_of_rows)   # 양식 및 cafe 데이터를 "add.html"에 템플린 랜더링

# All Cafe List Page - url 체계 - http://127.0.0.1:5000/cafes
@app.route('/cafes')
def cafes():
    # csv 파일 읽기 
    with open('cafe-data.csv', newline='') as csv_file:                 # cafe-data.csv를 읽기 모드로 열기 
        csv_data = csv.reader(csv_file, delimiter=',')                  # csv reader로 csv 파일 읽기
        list_of_rows = []                                               # 빈 리스트 선언 
        for row in csv_data:                                            
            list_of_rows.append(row)                                    # 읽은 데이터를 빈 리스트에 저장 
    return render_template('cafes.html', cafes=list_of_rows)            # 읽은 cafe 데이터를 "cafes.html"에 템플린 랜더링

# 애플리케이션 실행 - 디버그 모드 on
if __name__ == '__main__':
    app.run(debug=True)
