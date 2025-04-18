from flask import Flask, render_template 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insert_user")
def insert_user():
    return render_template("insert_user.html")

@app.route("/delete_user")
def delete_user():
    return render_template("delete_user.html")

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)