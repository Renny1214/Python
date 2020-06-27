import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "abc"
)

print(mydb)


#create a database
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE abc")

#check if database exists list of databse prints
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

#create a table
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE abc2  (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE TABLE abc3  (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


#to check if table exists
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


#any kind of query can be written within the execute statement
#"CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"    
#"ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"


#insert data into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
#mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#execute multiple rows
#val = [
#  ('Peter', 'Lowstreet 4'),
#  ('Amy', 'Apple st 652'),
#  ('Hannah', 'Mountain 21'),
#  ('Michael', 'Valley 345'),
#  ('Sandy', 'Ocean blvd 2'),
#  ('Betty', 'Green Grass 1'),
#  ('Richard', 'Sky st 331'),
#  ('Susan', 'One way 98'),
#  ('Vicky', 'Yellow Garden 2'),
#  ('Ben', 'Park Lane 38'),
#  ('William', 'Central st 954'),
#  ('Chuck', 'Main Road 989'),
#  ('Viola', 'Sideway 1633')
# ]
#mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#to print the last row id
sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
val = ("renny","1490")
#mycursor.execute(sql,val)
mydb.commit()
print("1 record inserted. ID :",mycursor.lastrowid)


#*select statement*

#prints all the data
mycursor.execute("select * from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#select only selected data
mycursor.execute("select name from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#fetch only one row
#mycursor.execute("select * from customers")
#myresult = mycursor.fetchone()
#print(myresult)

#where clause

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
#order by clause    
mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#delete clause
sql = "delete from customers where address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(S) deleted")

#drop table
mycursor = mydb.cursor()
sql = "drop table customers"
#mycursor.execute(sql)

sql="drop table if exists customers"
mycursor.execute(sql)


