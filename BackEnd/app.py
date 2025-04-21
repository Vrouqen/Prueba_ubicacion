from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

connDBUsers = mysql.connector.connect(
    host='dbusers',
    port=3306,  
    user='root',
    password='dbusers123',
    database='dbUsers'
)

connDBIncomes = mysql.connector.connect(
    host='dbincomes',
    port=3306,  
    user='root',
    password='dbincome123',
    database='dbIncomes'
)

connDBCosts = mysql.connector.connect(
    host='dbcosts',
    port=3306,  
    user='root',
    password='dbcost123',
    database='dbCosts'
)

@app.route("/users/login", methods=["POST"])
def login():
    # Form params
    username = request.form['username']
    password = request.form['password']

    cursorUsers = connDBUsers.cursor()
    cursorUsers.execute("SELECT * FROM Users")
    usersjson = cursorUsers.fetchall()

    for row in usersjson:
        if row[1]==username and row[2]==password:
            id_user = row[0]
            return jsonify({
                'message': 'Logged succesfully',
                'id_user': id_user
            })
    
    return jsonify({
        'message': 'Incorrect username or password',
        'id_user': 0
    })

@app.route("/users/insert_session", methods=["POST"])
def insert_session():

    id_user = request.form['id_user']
    log_in = request.form['log_in']
    date = datetime.now()

    cursorUsers = connDBUsers.cursor()
    cursorUsers.execute("INSERT INTO Users_Sessions (id_user, log_in, date) VALUES (%s, %s, %s)",(id_user, log_in, date,))
    
    connDBUsers.commit()
    cursorUsers.close()
    return jsonify({
        'message': 'Session inserted succesfully on DB'
    })


@app.route("/users/load_users", methods=["GET"])
def load_users():
    cursorUsers = connDBUsers.cursor()
    cursorUsers.execute("SELECT U.id_user, U.username, U.password, UI.name, UI.email, UI.description " \
    "FROM Users U, Users_Info UI WHERE U.id_user=UI.id_user;")
    usersjson = cursorUsers.fetchall()

    result = [{
        'id_user': row[0], 
        'username': row[1], 
        'password': row[2],
        'name': row[3], 
        'email': row[4], 
        'description': row[5]}
        for row in usersjson]

    cursorUsers.close()
    return {'result': result }

@app.route("/users/search_user/<id_user_search>", methods=["GET"])
def search_user(id_user_search):
    cursorUsers = connDBUsers.cursor()
    cursorUsers.execute("SELECT U.id_user, U.username, UI.name, UI.email, UI.description " \
    "FROM Users U, Users_Info UI WHERE U.id_user=UI.id_user and U.id_user=%s;", (id_user_search,))
    usersjson = cursorUsers.fetchall()

    result = {
        'id_user': usersjson[0][0], 
        'username': usersjson[0][1], 
        'name': usersjson[0][2],  
        'email': usersjson[0][3],  
        'description': usersjson[0][4]}
    
    cursorUsers.close()
    return {'result': result }

@app.route("/users/insert_user", methods=["POST"])
def insert_user():
    cursorUsers = connDBUsers.cursor()

    # Form params
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']
    description = request.form['description']

    # Definition of SQL instruction to insert on Users
    query = "INSERT INTO Users (username, password) VALUES (%s, %s);"
    cursorUsers.execute(query, (username, password))

    # Obtain the id_user auto generated
    query = "SELECT id_user FROM Users WHERE username=%s;"
    cursorUsers.execute(query, (username,))
    id_user = cursorUsers.fetchall() 

    # Definition of SQL instruction to insert on Users_Info
    query = "INSERT INTO Users_Info (id_user, name, email, description) VALUES (%s,%s,%s,%s);"
    cursorUsers.execute(query, (id_user[0][0], name, email, description))

    connDBUsers.commit()
    cursorUsers.close()

    return jsonify({'message': 'User inserted succesfully'})

@app.route("/users/delete_user", methods=["POST"])
def delete_user():
    cursorUsers = connDBUsers.cursor()

    # Definition of SQL instruction and get params of method
    query = "DELETE FROM Users WHERE id_user=%s"
    id_user = request.form['id_user']

    cursorUsers.execute(query, (id_user,))
    connDBUsers.commit()
    cursorUsers.close()
    
    return jsonify({'message': 'User deleted succesfully',
                    'user': id_user})

# Rutas para costo
@app.route("/costs/load_user_costs/<id_user>", methods=["GET"])
def load_users_costs(id_user):
    costscursor = connDBCosts.cursor()

    query = 'SELECT CN.name, C.value, C.date, TP.type_cost FROM Costs C, Costs_Names CN, Type_Cost TP ' \
    'WHERE C.id_user=%s and C.id_cost=CN.id_cost and C.id_cost=TP.id_cost;'

    costscursor.execute(query, (id_user,))
    costs_list = costscursor.fetchall()

    result = [{
        'name': c[0],
        'value': c[1],
        'date': c[2],
        'type_cost': c[3],
    }for c in costs_list]

    return jsonify({
        'result':result})

@app.route("/costs/insert_cost", methods=["POST"])
def insert_cost():
    costscursor = connDBCosts.cursor()
    
    id_user = request.form['id_user']
    name = request.form['name']
    value = request.form['value']
    date = request.form['date']
    type_cost = request.form['type_cost']

    query = "INSERT INTO Costs (id_user, value, date) VALUES (%s, %s, %s);"
    costscursor.execute(query, (id_user, value, date))
    
    query = "SELECT LAST_INSERT_ID();"
    costscursor.execute(query)
    id_cost = costscursor.fetchall()[0][0]

    query = "INSERT INTO Costs_Names (id_cost, name) VALUES (%s, %s);"
    costscursor.execute(query, (id_cost, name))

    query = "INSERT INTO Type_Cost (id_cost, type_cost) VALUES (%s, %s);"
    costscursor.execute(query, (id_cost, type_cost))
    
    connDBCosts.commit()
    return jsonify({
        'message': 'Cost inserted succesfully'
    })


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)