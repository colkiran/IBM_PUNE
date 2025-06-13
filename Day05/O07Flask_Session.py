from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "flask@123"
app.permanent_session_lifetime = timedelta(minutes=2)
@app.route("/")
def home():
    return render_template("index02.html", usrnm='Tyson', content="Fruits available in all seasons", Fruits=['Apple',
    'Orange', 'Grapes', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon', 'Blueberry', 'Mango'])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session['user'] = user
        return redirect(url_for("user", user="user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/users")
def user():
    if "user" in session:
        user = session['user']
        return f"<h2> {user} </h2>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)