import pandas as pd
import sqlite3


# connecting a new database with connect function.
connection = sqlite3.connect('mysqlite.db')
# cursor helps you query and execute database (to CRUD).
cursor = connection.cursor()

# delete table --> new create
cursor.execute('DROP TABLE CUSTOMER')


# create a table include name, email and phone number.
# ----WARNING: you have to change name of table because this table is exist on database.
cursor.execute('''
CREATE TABLE CUSTOMER(
EMAIL TEXT PRIMARY KEY,
NAME TEXT NOT NULL,
PHONE TEXT NOT NULL
);
''')

# add data to table.
cursor.execute('''
INSERT INTO CUSTOMER(EMAIL, NAME, PHONE)
VALUES
    ('tranquanghuy921819@gmail.com', 'huy', '0369461344'),
    ('thanhthaok05@gmail.com', 'thao', '0355904171');
               
''')

# commit it into database.
connection.commit()


# get any data by * operator.
data = pd.read_sql_query("SELECT * FROM CUSTOMER", connection)
print(data)
# result is in ../.image file.
