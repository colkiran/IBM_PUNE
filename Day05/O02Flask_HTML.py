
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route('/<username>')
def user(username):
    return render_template("index.html", usrnm = username)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
