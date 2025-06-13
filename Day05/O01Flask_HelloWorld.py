
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greetings Mr. {usrname}, Welcome to Flask Programming"

@app.route("/admin")
def admin():
    return redirect(url_for("user", usrname="ADMIN"))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)