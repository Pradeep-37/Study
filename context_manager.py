""" 
A context manager in Python is used to properly manage resources like files, network connections, 
or database connections. The most common way to use a context manager is with the "with" statement.
"""
# When working with resources like files or network connections, you must ensure that they are 
# properly closed after use.
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()  # Must remember to close the file
# If an error occurs before file.close(), the file remains open, potentially causing issues.

with open("example.txt", "w") as file:
    file.write("Hello, World!")  # No need to manually close the file
# The with statement automatically closes the file when the block exits.
# Even if an exception occurs, the file is properly closed.

#Python's contextlib module provides an easier way to create context managers
# using the @contextmanager decorator.
#Managing Database Connections
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_name):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()  # Ensures the connection is closed

# Using the context manager
with db_connection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()

#  Ensures the database connection is always closed, even if an error occurs.

