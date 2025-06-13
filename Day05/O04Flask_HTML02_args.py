
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Flask Programming </h1>"

@app.route("/<username>")
def user(username):
    return render_template("index02.html", content = "Fruits available in all seasons", usrnm = username, fruits = ['Apple', 'Orange', 'Pineapple', 'Mango',
        'Banana', 'Strawberry', 'Blueberry'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader= True)
