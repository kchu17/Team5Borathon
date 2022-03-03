from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! This file was edited locally.</h1>"

@app.route("/GetCustomerAccountByAccountNumber")
def getCustomerAccountByAccountNumber():
    return "<h1 style='color:blue'>Getting Customer Account By Account Number.</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


