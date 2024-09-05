import psycopg2

conn = psycopg2.connect(
    dbname="Store",
    user="postgres",
    password="123",
    host="37.32.5.219",
    port="5432"
)

cur = conn.cursor()

#select
cur.execute('SELECT * FROM "Customer"')
rows = cur.fetchall()
for row in rows:
    print(row)
    
 



    
conn.commit()

cur.close()
conn.close()







# Connect to your postgres DB
# connection = psycopg2.connect(
#     dbname='Store',
#     user='postgres',
#     password='123',
#     host='37.32.5.219',
#     port=5432
# )


# conn = psycopg2.connect("dbname=dvdrental user=postgres")

# Open a cursor to perform database operations
# cur = connection.cursor()

# Execute a query
# cur.execute('SELECT "Customer_id", name FROM "Customer";')
# cur.execute('''INSERT INTO public."Customer" ("Customer_id", Name) VALUES (7, 'sakkaki');''')
# cur.execute('''DELETE from public."Customer" where "Customer_id"=6''')
# cur.execute('''UPDATE "Customer" SET Name = 'Alfred Schmidt' WHERE "Customer_id" = 3;''')

# Retrieve query results
# connection.commit()
# records = cur.fetchall()
# for item in records:
#     print(item * 2)
# print(records)
# connection.close()