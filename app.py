from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask2'

mysql = MySQL(app)


@app.route('/')
def hello():
    return "<h1>Hello<h1>"


@app.route('/user', methods=['POST', 'GET'])
def my_data():
    data = request.get_json()
    ##daty = type(data)

    return print(data)


@app.route('/userr', methods=['POST', 'GET'])
def post():
    req_data = request.get_json()
    user_id = req_data['id']
    name = req_data['name']
    email = req_data['email']
    phone = req_data['phone']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(id, name, email, phone) VALUES (%s, %s, %s, %s)", (user_id, name, email, phone))
    mysql.connection.commit()
    return jsonify({"Error": "false", "message": {"response":"success", "user_id": user_id}})

@app.route('/users', methods=['POST', 'GET'])
def get():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    result = []

    for row in data:
        result.append({"id": row[0], "email": row[1], "password": row[2], "name": row[3], "school": row[4]})

    return jsonify(result)    
    ##for row in data:
    ##    return jsonify({"id": row[0], "email": row[1], "password": row[2], "name": row[3], "school": row[4]})



@app.route('/addUser', methods=['POST', 'GET'])
def add():
    req_data = request.get_json()
    id = 5
    email = req_data['email']
    password = req_data['password']
    name = req_data['name']
    school = req_data['school']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(id, email, password, name, school) VALUES (%s, %s, %s, %s, %s)", (id, email, password, name, school))
    mysql.connection.commit()
    return jsonify({"Error": "false", "message": {"response":"success",}})




if __name__ == "__main__":
    app.run(debug = True)
