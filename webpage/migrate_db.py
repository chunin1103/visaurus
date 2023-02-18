import psycopg2
import csv

conn = psycopg2.connect(database="postgres", user="postgres", password="Neji1103!!", host="database-thesaurus.crnbbf6rv4rc.ap-southeast-1.rds.amazonaws.com", port="5432")
cur = conn.cursor()

n=0
with open('db_extract.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        word = row[0]
        synonyms = row[1] if row[1] != "" else None
        n+=1
        cur.execute("INSERT INTO synonyms (word, synonyms) VALUES (%s, %s)", (word, synonyms))
        print(n)

conn.commit()
cur.close()
conn.close()
