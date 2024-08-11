'''
What is connector?

Connector is a tool/module in python whiich helps us to establish connection with the database running
in another server.

Why we use it?
To fetch data or store data in a database(where we keep our data) and later retrieve/fetch/search it

How we use it?
by using python connecotr for mysql
mysql.connector--module
mysql.connector.connect()

'''

import mysql.connector

mydb=mysql.connector.connect(
    host='127.0.0.1',
    username="root",
    password="password",
    database="databasename"
)
obj=mydb.cursor()

#obj.execute("create database Registration")
#obj.execute('use registration')
#obj.execute('create table UserMobileRegistration(sl int primary key,name varchar(30),mobileNumber varchar(13))')
obj.execute('select * from student')
r=obj.fetchall()
print(r)

