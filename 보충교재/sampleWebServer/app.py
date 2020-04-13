from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is post 1 ....',
        'author': 'YJ'
    },
    {
        'title': 'Post 2',
        'content': 'This is post 2 ....'
    }
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def post():
    return render_template("posts.html", posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name + ", your id is " + str(id)

@app.route('/onlyget', methods=['POST'])
def get_req():
    return "You can only get this web page 2"

if __name__ == '__main__':
    app.run(debug=True)