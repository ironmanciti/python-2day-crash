from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome Home !!!"

@app.route("/python/")
def python():
    return "<h1>알고리즘으로 배우는 파이썬</h1>"

@app.route("/home/<string:name>")
def home(name):
    return f"Welcome Home {name}"

if __name__ == "__main__":
    app.run(debug=True)


