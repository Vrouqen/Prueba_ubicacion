from flask import Flask, render_template, session, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/insert_user")
def insert_user():
    return render_template("insert_user.html")

@app.route("/delete_user")
def delete_user():
    return render_template("delete_user.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)