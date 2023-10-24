from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    this_year = datetime.now().year
    return render_template("index.html", num=random_number, year=this_year)

if __name__ == '__main__':
    app.run(debug=True)