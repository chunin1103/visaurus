import csv

with open('86k.csv', encoding='utf8') as f:
    row = f.readlines()
    
for i in row:
    content = list(row[i] for i in "Symnonym")
print(content)