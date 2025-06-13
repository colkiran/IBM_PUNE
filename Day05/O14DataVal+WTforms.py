
from flask import Flask, request
from forms import UserForm
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "<h1> Hello World </h1>"

@app.route("/submit", methods=['POST'])
def submit():
    form = UserForm(request.form)
    if form.validate():
        username = request.form['username']
        email = request.form['email']
        return f"Name is {username} Email is {email}"
    else:
        return "Invalid form entry....."

if __name__ == '__main__':
    app.run(debug=True)
