import sqlite3

with sqlite3.connect("netflix.db") as connection:
    cursor = connection.cursor()
    cursor.execute("our commands will be here")
