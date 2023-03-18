import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("synonyms.db")
cursor = conn.cursor()

# Create the table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS symnonyms (
    word TEXT NOT NULL,
    synonyms TEXT NOT NULL
);
""")

# Read the data from the CSV file
with open("db_extract_ver3.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        word = row[0]
        synonyms = row[1]
        cursor.execute("""
            INSERT INTO symnonyms (word, synonyms)
            VALUES (?, ?)
        """, (word, synonyms))

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()