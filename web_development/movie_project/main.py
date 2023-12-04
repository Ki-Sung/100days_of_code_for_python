from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# DB 생성 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 데이터 베이스 내 테이블 정의
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# 더미 데이터 - 실행하고 주석 처리하기 
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://en.wikipedia.org/wiki/File:Phone_Booth_movie.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    movies = db.session.query(Movie).all()
    return render_template("index.html", movies=movies)

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         new_movie = Movie(
#             title=request.form["title"],
#             year=request.form["year"],
#             description=request.form["description"],
#             rating=request.form["rating"],
#             ranking=request.form["ranking"],
#             review=request.form["review"],
#             img_url=request.form["img_url"]
#         )
#         db.session.add(new_movie)
#         db.session.commit()
        
#         return redirect(url_for("home"))
    
#     return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)
