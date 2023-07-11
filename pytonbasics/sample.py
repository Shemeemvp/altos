import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user = 'root', database = 'mydatabase');
mycursor = mydb.cursor()

# mycursor.execute('create database mydatabase');
'''mycursor.execute('show databases')

for x in mycursor:
    print(x)'''

# TABLE CREATION
# mycursor.execute('create table customer(name varchar(50), address varchar(100))')
'''mycursor.execute('show tables')
for x in mycursor:
    print(x)'''

# PRIMARY KEY 
# mycursor.execute('create table person(id int auto_increment primary key, name varchar(50), age int)');

# INSERTION

'''sql = 'insert into person (name,age) values (%s,%s)'
value = ('Arjun',25)
mycursor.execute(sql,value);
mydb.commit()
print(mycursor.rowcount,'Record inserted..')'''


# MULTIPLE INSERTION
'''sql = 'insert into person (name,age) values (%s,%s)';
value = [('Abhi',22),('Ashik',23),('Ajay',28),('karthi',40)]
mycursor.executemany(sql,value)
mydb.commit()
print(mycursor.rowcount, 'records inserted..')'''


# SELECTION
'''mycursor.execute('select * from person');
myresult = mycursor.fetchall();
for x in myresult:
    print(x)'''

'''mycursor.execute('select * from person');
myresult = mycursor.fetchone();
print(myresult)'''

# SELECTION USING WHERE CONDITION
'''sql = 'select * from person where name = "Arjun"'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

'''sql = 'select * from person where name like "a_%"'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

# SORTING
'''sql = 'select * from person order by name'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

'''sql = 'select * from person order by name desc'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

# DELETION
'''sql = 'delete from person where id = 4'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, 'deleted..')'''

# UPDATION
'''sql = 'update person set name ="shemeem" where id = 2'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, 'row updated..')'''

# SELECTION USING LIMIT AND OFFSET
'''mycursor.execute('select * from person limit 3')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''

'''mycursor.execute('select * from person limit 3 offset 2')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)'''