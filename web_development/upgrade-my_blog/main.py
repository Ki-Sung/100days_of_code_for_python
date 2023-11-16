import requests
from flask import Flask, render_template

# 플라스크 객체 선언 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about_blog():
    return render_template("about.html")

@app.route('/contact')
def contact_me():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)