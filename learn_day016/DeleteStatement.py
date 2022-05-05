import mysql.connector as connection
import learn_day016.DBUtil as util

delete_query = "DELETE FROM actor WHERE actor_id = %s;"
values = [("274",),("273",)]

conn = util.make_connection()
db_cursor = conn.cursor()
db_cursor.executemany(delete_query, values)
conn.commit()
print("Number of rows deleted " ,db_cursor.rowcount)
db_cursor.close()
util.close_connection(conn)