import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('synonyms.db')

# Export data to CSV file
df = pd.read_sql_query("SELECT * from symnonyms", conn)
df.to_csv('db_extract.csv', index=False)