
from flask import Flask, render_template, make_response, request
import time
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index02.html", usrnm='Tyson', content="Fruits available in all seasons",fruits=['Apple', 'Orange', 'Grapes', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon','Blueberry', 'Mango'])


@app.route("/set_cookie")
def set_cookie():
    targetTime = time.time() + 60           # 60 Secs
    resp = make_response("Success")
    resp.set_cookie("Prod1", "Pepsi", expires=targetTime)
    resp.set_cookie("Prod2", "Sprite", expires=targetTime)
    return resp

@app.route("/get_cookie")
def get_cookie():
    prd1 = request.cookies.get('Prod1')
    prd2 = request.cookies.get('Prod2')
    if prd1 == None:
        prd1 = "Cookie Deleted..."
    if prd2 == None:
        prd2 = "Cookie Deleted....."
    return f"<h2> First Cookie :{prd1} <br> Second Cookie :{prd2} </h2>"

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)

