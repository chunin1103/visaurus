import csv
from google_translate3 import *
import csv
from encodings import utf_8

# open the file in the write mode
f = open('symnonyms_vi.csv', 'w', encoding="utf-8", newline='')
# create the csv writer
writer = csv.writer(f)

sym_list =[]
n = 0
with open('Symnonym_List.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    # structure: [{"Word": "abcd", "Symnonym": ["abc", "def"]}]
    for i in reader:
        n+=1
        if n<20:
            tu_dn = i["Symnonyms"]
            tu_dn = [tu_dn]
            for i in tu_dn:
                vie_sym = GGtrans(i)
                vie_sym = [vie_sym]
                sym_list.append(vie_sym)

for i in sym_list:
    writer.writerow(i)
            
            # sym_list.append(i["Symnonyms"])
# print(sym_list)