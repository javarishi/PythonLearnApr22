import mysql.connector as connection
import learn_day016.DBUtil as util

select_query = "SELECT actor_id, first_name, last_name, last_update FROM actor WHERE first_name LIKE %s ORDER BY first_name"
values = ("A%",)

conn = util.make_connection()
db_cursor = conn.cursor()
db_cursor.execute(select_query, values)
select_results = db_cursor.fetchall()

for each_row in select_results:
    print(each_row, type(each_row))

db_cursor.close()
util.close_connection(conn)