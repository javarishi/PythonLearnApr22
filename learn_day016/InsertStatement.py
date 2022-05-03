import mysql.connector as connection
import learn_day016.DBUtil as util

insert_query = "INSERT INTO actor (first_name,last_name,last_update) VALUES (%s,%s, CURRENT_TIMESTAMP)"
values = [("Clark", "Kent"),
          ('Kara', "Danver"),
          ('Berry', "Alan")
          ]

conn = util.make_connection()
db_cursor = conn.cursor()
db_cursor.executemany(insert_query, values)
conn.commit()
print("record inserted, ID:", db_cursor.lastrowid)
print("Number of rows affected " ,db_cursor.rowcount)
db_cursor.close()
util.close_connection(conn)