from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insert_user")
def insert_uset():
    return render_template("insert_user.html")

if __name__=="__main__":
    app.run(debug=True, port=8080)