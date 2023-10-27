import requests
from post import Post
from flask import Flask, render_template

# 블로그 포스트 내용 API로 제어 
posts = requests.get("https://api.npoint.io/82bc7d5d46906ffb9ed4").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

# 플라스크 객체 선언 
app = Flask(__name__)

# Home 페이지 구조
@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

# 블로그 포스트 페이지 구조 
@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
