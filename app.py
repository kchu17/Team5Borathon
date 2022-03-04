from random import randint, random
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

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/GetCustomerAccountByAccountNumber", methods=['GET'])
def getCustomerAccountByAccountNumber():
    accountNumber = request.args.get('accountNumber')

    cur = conn.cursor()
    cur.execute("SELECT * FROM Account WHERE accountNumber = %s;", accountNumber)
    account = cur.fetchall()[0]
    print(account[0])

    cur = conn.cursor()
    cur.execute("SELECT firstName, lastName FROM Customer WHERE accountID = %s;", account[0])
    customer = cur.fetchall()[0]
    print(customer)

    my_dict = {'firstName': customer[0], 'lastName': customer[1], 'accountNumber':account[1], 'balance' : account[2], 'status' : account[3]}

    return jsonify(my_dict)

@app.route("/OpenCustomerAccount", methods=['POST'])
def OpenCustomerAccount():
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    
    accountNumber = randint(0,10000)
    balance = 0
    status = "Open"

    cur = conn.cursor()
    cur.execute("INSERT INTO Account (accountNumber,balance,status) VALUES (%s,%s,%s)", (accountNumber,balance,status))
    conn.commit()

    cur = conn.cursor()
    cur.execute("SELECT LAST_INSERT_ID();")
    accountID = cur.fetchall()[0]
    print(accountID, accountNumber)

    cur = conn.cursor()
    cur.execute("INSERT INTO Customer (firstName,lastName,accountID) VALUES (%s,%s,%s)", (firstName,lastName,accountID))
    conn.commit()


    my_dict = {'firstName': firstName, 'account': accountNumber}
    print(my_dict)
    return jsonify(my_dict)

@app.route("/CloseCustomerAccount", methods=['POST'])
def CloseCustomerAccount():
    accountNumber = request.args.get('accountNumber')

    cur = conn.cursor()
    cur.execute("UPDATE Account SET status = %s WHERE accountNumber = %s;", ("Closed", accountNumber))
    conn.commit()

    cur = conn.cursor()
    cur.execute("SELECT balance,status,accountID FROM Account WHERE accountNumber = %s;", accountNumber)
    balance,status,accountID = cur.fetchall()[0]

    cur = conn.cursor()
    cur.execute("SELECT firstName, lastName FROM Customer WHERE accountID = %s;", accountID)
    customer = cur.fetchall()[0]
    print(customer)
    

    my_dict = {'firstName': customer[0], 'lastName': customer[1], 'accountNumber':accountNumber, 'balance' : balance, 'status' : status}

    return jsonify(my_dict)

@app.route("/ApplyTransactionToCustomerAccountAsync", methods=['POST'])
def ApplyTransactionToCustomerAccountAsync():
    accountNumber = request.args.get('accountNumber')
    amount = float(request.args.get('amount'))
    transactionType = request.args.get('transactionType')


    cur = conn.cursor()
    cur.execute("SELECT balance,accountID FROM Account WHERE accountNumber = %s;", accountNumber)
    balance,accountID = cur.fetchall()[0]

    cur = conn.cursor()
    cur.execute("INSERT INTO Transaction (amount,transactionType,accountID) VALUES (%s,%s,%s)", (amount,transactionType,accountID))
    conn.commit()

    if transactionType == "Credit":
        pass
    elif transactionType == "Debit":
        amount = 0 - amount

    cur = conn.cursor()
    cur.execute("UPDATE Account SET balance = %s WHERE accountNumber = %s;", (balance + amount, accountNumber))
    conn.commit()

    

    cur = conn.cursor()
    cur.execute("SELECT firstName, lastName FROM Customer WHERE accountID = %s;", accountID)
    customer = cur.fetchall()[0]
    print(customer)
    cur = conn.cursor()
    cur.execute("SELECT balance,status FROM Account WHERE accountNumber = %s;", accountNumber)
    balance,status = cur.fetchall()[0]

    my_dict = {'firstName': customer[0], 'lastName': customer[1], 'accountNumber':accountNumber, 'balance' : balance, 'status' : status}

    return jsonify(my_dict)

@app.route("/GetJohnTest", methods=['GET'])
def getJohnTest():
    result = get_details()
    my_dict = {'firstName': 'Belissa', 'account': result}
    return jsonify(my_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


