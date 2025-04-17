from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conn1 = mysql.connector.connect(
    host='localhost',
    port=1001,  
    user='root',
    password='dbusers123',
    database='dbUsers'
)

conn2 = mysql.connector.connect(
    host='localhost',
    port=1002,  
    user='root',
    password='dbincome123',
    database='dbIncomes'
)

conn3 = mysql.connector.connect(
    host='localhost',
    port=1003,  
    user='root',
    password='dbcost123',
    database='dbCosts'
)

@app.route("/users/load_users", methods=["GET"])
def load_users():
    cursorUsers = conn1.cursor()
    cursorUsers.execute("SELECT * FROM Users")
    usersjson = cursorUsers.fetchall()
    cursorUsers.close()

    result = [{
        'id_user': row[0], 
        'username': row[1], 
        'password': row[2]} 
        for row in usersjson]

    return {'result': result }

@app.route("/users/insert_user", methods=["POST"])
def insert_user():
    cursorUsers = conn1.cursor()

    # Definition of SQL instruction and get params of method
    query = "INSERT INTO Users (username, password) VALUES (%s, %s);"
    user = request.form['user']
    password = request.form['password']

    cursorUsers.execute(query, (user, password))
    conn1.commit()
    cursorUsers.close()

    return jsonify({'message': 'User inserted succesfully',
                    'user': user+" "+password})

@app.route("/users/delete_user", methods=["POST"])
def delete_user():
    cursorUsers = conn1.cursor()

    # Definition of SQL instruction and get params of method
    query = "DELETE FROM Users WHERE id_user=%s"
    id_user = request.form['id_user']

    cursorUsers.execute(query, (id_user,))
    cursorUsers.close()
    
    return jsonify({'message': 'User deleted succesfully',
                    'user': id_user})

if __name__=="__main__":
    app.run(debug=True, port=8081)