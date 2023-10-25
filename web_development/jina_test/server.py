from flask import Flask, render_template

import random
import requests
from datetime import datetime

app = Flask(__name__)

# 홈 주소 체계 및 기능
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    this_year = datetime.now().year
    return render_template("index.html", num=random_number, year=this_year)

# 이름으로 나이, 성별 맞추기 사이트 주소 체계 및 기능
@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    
    this_year = datetime.now().year
    return render_template("guess.html", person_name=name, gender=gender, age=age, year=this_year)

# 블로그 포스트 내용 API 
@app.route('/blog/<number>')
def get_blog(number):
    print(number)
    blog_url = "https://api.npoint.io/82bc7d5d46906ffb9ed4"
    reponse = requests.get(blog_url)
    all_posts = reponse.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)