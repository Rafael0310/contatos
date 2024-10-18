import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='estudo',
    user='Rafael',
    password='Raft-0310'
)

cursor = conn.cursor()