# This is still a work in progress.
# A lot of this will be tutorials, documents, and somewhat messy code as I learn

import sqlite3

# If the parameter in "example.db" has not yet been created, sqlite3 will create it automatically
connection = sqlite3.connect("example.db")

# We need a cursor to interact with our database systems
# cursor_variable = db_variable.cursor_variable()
cursor = connection.cursor()

# Let's us execute db queries through Python
# Be sure to run this file, otherwise your database won't appear
cursor.execute('''CREATE TABLE IF NOT EXISTS tshirts
                (sku text PRIMARY KEY, name text, size, price real)''') # column-header, data type
# The sku text PRIMARY KEY sets itself as the primary key

# You might expect this data to be inserted and ready to go, but this code needs to be committed
# INSERT OR IGNORE is a good way to avoid tracebacks if you have made an error in insertion
cursor.execute('''INSERT OR IGNORE INTO tshirts VALUES 
                        ('SKU1235', 'Black logo Tshirt', 'Large', '24.99')''')

# This will officially add the data to the databases, and commit the changes like Github for example
connection.commit()

# Unlike printing a usual line of code or a variable, everytime you run this code it will save the data
# If ran three times, it would print ('SKU1234', 'Black logo Tshirt', 'Medium', 24.99) three times
for row in cursor.execute('''SELECT * from tshirts'''):
    print(row)

# It's not ideal to insert this data over and over. This is where the use of a primary key comes in
# A primary key will allow only one instance of that value