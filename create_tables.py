import pymysql

conn = pymysql.connect(
        host= 'team5db-1.cjh7bpk5je23.us-east-1.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'Random!PassT5#',
        db = 'bankDB',
        )


# create table
with conn.cursor() as cur:
    cur.execute('create table testTable1 (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20));')

# alternative    
# cursor=conn.cursor()
# create_table="""
# create table testTable1 (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20))
# """
# cursor.execute(create_table)