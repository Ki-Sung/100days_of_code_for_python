from flask import Flask, render_template

app = Flask(__name__)

# saple용 코드 
# @app.route('/')
# def home():
#     return render_template("gilbert_sample.html")

# main 페이지 - html 랜더링
@app.route('/')
def hello_world():
    return render_template("index.html")
            
if __name__ == '__main__':
    app.run(debug=True)