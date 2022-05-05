import mysql.connector as connection
import learn_day016.DBUtil as util

update_query = "UPDATE actor SET first_name = %s, last_name = %s, last_update = CURRENT_TIMESTAMP WHERE actor_id = %s;"
values = ("Klark", "Kent", "261")

conn = util.make_connection()
db_cursor = conn.cursor()
db_cursor.execute(update_query, values)
conn.commit()
print("Number of rows affected " ,db_cursor.rowcount)
db_cursor.close()
util.close_connection(conn)