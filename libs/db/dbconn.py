#database connect
import sqlite3

def getconn():
    conn= sqlite3.connect('c:/pydb/mydb.db')
    return conn

