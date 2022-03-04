from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
        host= 'team5db-1.cjh7bpk5je23.us-east-1.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'Random!PassT5#',
        db = 'bankDB',
        )

# create DB
# with conn.cursor() as cur:
#     cur.execute('create database bankDB;')

# create table
# cursor=conn.cursor()
# create_table="""
# create table testTable1 (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20))
# """
# cursor.execute(create_table)

def insert_details(name,email,comment,gender):
    cur = conn.cursor()
    cur.execute("INSERT INTO testTable1 (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
    conn.commit()
#insert_details("John", "john@mail.com","Testing from DB", "Male")   

def get_details():
    cur = conn.cursor()
    cur.execute("SELECT * FROM testTable1")
    details = cur.fetchall()
    return details

# def select(name):
#     cur=conn.cursor()
#     cur.execute("SELECT comment FROM testTable1 WHERE name = %s", (name,email,comment,gender))
#     conn.commit()

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/GetCustomerAccountByAccountNumber", methods=['GET'])
def getCustomerAccountByAccountNumber():
    accountNumber = request.args.get('accountNumber')
    my_dict = {'firstName': 'Belissa', 'account': accountNumber}
    return jsonify(my_dict)

@app.route("/GetJohnTest", methods=['GET'])
def getJohnTest():
    result = get_details()
    my_dict = {'firstName': 'Belissa', 'account': result}
    return jsonify(my_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


