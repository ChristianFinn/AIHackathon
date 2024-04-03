import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table with unique fields
cursor.execute('''
    CREATE TABLE IF NOT EXISTS your_table (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        email TEXT UNIQUE
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()