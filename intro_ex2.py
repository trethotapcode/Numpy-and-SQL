import pandas as pd
import sqlite3

connection = sqlite3.connect('mysqlite.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE PRODUCT')

# create table
cursor.execute('''  CREATE TABLE PRODUCT(
               ID INTEGER PRIMARY KEY,
               NAME TEXT NOT NULL,
               PRICE INTEGER NOT NULL
               );
''')


# add first data
cursor.execute('''INSERT INTO PRODUCT(ID, NAME, PRICE)
VALUES
               (1, 'iPhone 15', 18000000),
               (2, 'Galaxy Z-Fold 4', 30000000);
''')

connection.commit()

# update data
cursor.execute('''
UPDATE PRODUCT
SET PRICE = 50000000
WHERE 1 = 1
AND ID = 2
               ''')
connection.commit()

# delete iPhone
cursor.execute('''DELETE FROM PRODUCT
                WHERE 1 = 1
                AND NAME = 'iPhone 15'  ''')
connection.commit()

data = pd.read_sql_query('SELECT * FROM PRODUCT', connection)
print(data)
