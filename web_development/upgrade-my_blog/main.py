import requests
from post import Post
from flask import Flask, render_template

# 블로그 포스트 내용 API 제어 
posts = requests.get("https://api.npoint.io/37689f9426dd018a0fd4").json()   # API 엔드포인트의 JSON 데이터 가져오기 

# 플라스크 객체 선언 
app = Flask(__name__)

# main 페이지 
@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)

# about page 
@app.route('/about')
def about_blog():
    return render_template("about.html")

# contact page 
@app.route('/contact')
def contact_me():
    return render_template("contact.html")

# 블로그 포스트 페이지 구조 
@app.route('/post/<int:index>')
def blog_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)