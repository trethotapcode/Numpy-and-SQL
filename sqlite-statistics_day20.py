import pandas as pd
import sqlite3

connection = sqlite3.connect('mysqlite.db')
cursor = connection.cursor()

# refresh data-table
cursor.execute('DROP TABLE STOCK')

# create table.
cursor.execute(
    '''
CREATE TABLE STOCK(
ID INTEGER PRIMARY KEY,
NAME TEXT NOT NULL,
BUY INTEGER NOT NULL,
INVESTOR TEXT NOT NULL);
'''
)

# insert data
cursor.execute('''
INSERT INTO STOCK
VALUES
    (1, 'ACB', 29.45, 'Nguyen'),
    (2, 'VIC', 44.55, 'Nguyen'),
    (3, 'GMD', 74.30, 'Nguyen'),
    (4, 'ACB', 28.45, 'Vinh'),
    (5, 'VIC', 40.55, 'Vinh'),
    (6, 'GMD', 60.30, 'Vinh');
''')

# query sum of stock
query = '''
SELECT SUM(BUY) AS total_revenue
FROM STOCK
'''


# query max_price of each investor. For example, Nguyen buys GMD as price 74.30$.
second_query = '''
SELECT INVESTOR, NAME, MAX(BUY) AS MAX_PRICE
FROM STOCK
GROUP BY INVESTOR
'''


data = pd.read_sql_query(query, connection)
print(data)

print()

second_data = pd.read_sql_query(second_query, connection)
print(second_data)
