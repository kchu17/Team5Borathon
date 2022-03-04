import pymysql

conn = pymysql.connect(
        host= 'team5db-1.cjh7bpk5je23.us-east-1.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'Random!PassT5#',
        db = 'bankDB',
        )

# CREATE TABLE Account (
#     accountID INT NOT NULL,
#     accountNumber VARCHAR(200) NOT NULL,
#     balance FLOAT NOT NULL,
#     status VARCHAR(200) NOT NULL,
#     PRIMARY KEY (accountID),
# );

#ALTER TABLE Account ADD accountID INT NOT NULL AUTO_INCREMENT;

# CREATE TABLE Customer (
#     customerID INT NOT NULL,
#     firstName VARCHAR(200) NOT NULL,
#     lastName VARCHAR(200) NOT NULL,
#     PRIMARY KEY (customerID),
#     accountID INT NOT NULL,
#     FOREIGN KEY (accountID) REFERENCES Account(accountID)
# );

# CREATE TABLE Transaction (
#     transactionID INT NOT NULL,
#     amount FLOAT NOT NULL,
#     transactionType VARCHAR(200) NOT NULL,
#     PRIMARY KEY (transactionID),
#     accountID INT NOT NULL,
#     FOREIGN KEY (accountID) REFERENCES Account(accountID)
# );

# - ---------- Actual code ----------
# create Account table
with conn.cursor() as cur:
    cur.execute('CREATE TABLE Account (accountID INT NOT NULL AUTO_INCREMENT, accountNumber VARCHAR(200) NOT NULL, balance FLOAT NOT NULL, status VARCHAR(200) NOT NULL, PRIMARY KEY (accountID));')

# # addin auto increment to Account table
# with conn.cursor() as cur:
#     cur.execute('ALTER TABLE Account MODIFY accountID INT NOT NULL AUTO_INCREMENT;')

# with conn.cursor() as cur:
#     cur.execute('ALTER TABLE Customer ADD customerID INT NOT NULL AUTO_INCREMENT;')

# with conn.cursor() as cur:
#     cur.execute('ALTER TABLE Transaction ADD transactionID INT NOT NULL AUTO_INCREMENT;')


# create Customer table
with conn.cursor() as cur:
    cur.execute('CREATE TABLE Customer (customerID INT NOT NULL AUTO_INCREMENT, firstName VARCHAR(200) NOT NULL, lastName VARCHAR(200) NOT NULL, PRIMARY KEY (customerID), accountID INT NOT NULL, FOREIGN KEY (accountID) REFERENCES Account(accountID));')

# create Transaction table
with conn.cursor() as cur:
    cur.execute('CREATE TABLE Transaction (transactionID INT NOT NULL AUTO_INCREMENT, amount FLOAT NOT NULL, transactionType VARCHAR(200) NOT NULL, PRIMARY KEY (transactionID), accountID INT NOT NULL, FOREIGN KEY (accountID) REFERENCES Account(accountID));')

 