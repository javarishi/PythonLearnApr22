import mysql.connector as connection


def make_connection():
    conn = connection.connect(
        host="localhost",
        port="3306",
        database="sakila",
        user="root",
        password="password")
    return conn


def close_connection(conn):
    conn.close()




