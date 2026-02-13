import mysql.connector
host = 'localhost'
user = 'root'
password = 'admin@0202'
database = 'selenium-python'


conn=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor=conn.cursor()
print("connected to the database")

query="select * from employee;"
cursor.execute(query)

result=cursor.fetchall()
for row in result:
    print(row)
print(result)