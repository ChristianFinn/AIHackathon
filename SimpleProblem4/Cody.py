import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Add unique constraint on symbol column
c.execute('CREATE UNIQUE INDEX idx_symbol ON stocks(symbol)')

# Try inserting duplicate symbol
try:
  c.execute("INSERT INTO stocks VALUES ('2006-01-07','SELL','GBP',200,4.14)") 
except sqlite3.IntegrityError:
  print('ERROR: Could not insert duplicate symbol')

# Close connection
conn.close()
