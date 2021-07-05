from flask import Flask, render_template, request
from flask import url_for


app = Flask(__name__)


@app.route("/")
def index():
    print("test")
    return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/users", methods=['POST', 'GET'])
def users():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            surname = request.form.get('surname')
            username = request.form.get('username')
            password = request.form.get('password')

            return render_template("users.html", name=name, surname=surname, username=username, password=password)
    except:
        return render_template("users.html", hata="hata oluştu")


if __name__ == "__main__":
    app.run(debug=True, port=3000)