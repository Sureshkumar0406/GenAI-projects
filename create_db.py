import sqlite3

# Connect to the Chinook database (use the correct path to your file)
conn = sqlite3.connect(r'C:\Users\sures\Final_projects\GenAI\SQL_chatbot\chinook_db.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()


# Open the .sql file and read its contents
with open('chinook_Sqlite.sql', 'r',encoding='utf-8', errors='ignore') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

print("Database created and data inserted successfully!")


# List all tables to find the correct table name
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table)

# Example query: Get all artists from the database
cursor.execute("SELECT * FROM Artist")
artists = cursor.fetchall()

# Print the result
for artist in artists:
     print(artist)

# Close the connection

# Commit changes and close the connection
conn.commit()
# conn.close()