import os
from dotenv import load_dotenv
import requests
import smtplib
from flask import Flask, render_template, request

# 블로그 포스트 내용 API 제어 
posts = requests.get("https://api.npoint.io/37689f9426dd018a0fd4").json()   # API 엔드포인트의 JSON 데이터 가져오기 

# dotenv 로드 
load_dotenv(verbose=True)

# 상수 설정 - 이메일 정보 
MY_EMAIL = os.getenv("MY_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")

# 플라스크 객체 선언 
app = Flask(__name__)

# main 페이지 
@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

# 블로그 포스트 페이지 구조 
@app.route('/post/<int:index>')
def blog_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# about page 
@app.route('/about')
def about_blog():
    return render_template("about.html")

# contact form 
@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    
    return render_template("contact.html", msg_sent=False)

# smtplib - send mail
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GOOGLE_APP_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)