
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Flask Programming </h1>"

@app.route("/<username>")
def user(username):
    return render_template("index01.html", usrnm = username, content = "for loop......")

if __name__ == '__main__':
    app.run(debug=True, use_reloader= True)
