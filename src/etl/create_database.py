import sqlite3

# Create/connect to database
conn = sqlite3.connect("db/nifty100.db")

# Read SQL schema
with open("db/schema.sql", "r", encoding="utf-8") as f:
    schema = f.read()

# Execute schema
conn.executescript(schema)

conn.commit()
conn.close()

print("✅ Database created successfully!")