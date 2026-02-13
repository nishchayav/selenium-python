import mysql.connector

host = 'localhost'
user = 'root'
password = 'admin@0202'
database = 'selenium-python'

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
print("Connected to the database")


print("\nEmployees with salary > 50000:")
fetch_query = "SELECT * FROM employee WHERE empSALARY > %s"
cursor.execute(fetch_query, (50000,))
results = cursor.fetchall()

for row in results:
    print(row)


insert_query = """
INSERT INTO employee (empID, empNAME, empSALARY)
VALUES (%s, %s, %s)
"""
cursor.execute(insert_query, (4, "TestUser4", 100000))
conn.commit()
print("\nNew employee inserted successfully!")


update_query = """
UPDATE employee
SET empSALARY = empSALARY * 1.10
WHERE empNAME = %s
"""
cursor.execute(update_query, ("TestUser",))
conn.commit()
print("Salary updated by 10% successfully!")

cursor.close()
conn.close()
