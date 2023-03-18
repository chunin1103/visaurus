import csv
from google_translate3 import *
import csv
from encodings import utf_8
import time

# open the file in the write mode
f = open('symnonyms_vi_onelook.csv', 'w', encoding="utf-8", newline='')
# create the csv writer
writer = csv.writer(f)

sym_list =[]
with open('symnonyms_eng_onelook.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    # structure: [{"Word": "abcd", "Symnonyms": ["abc", "def"]}]
    for i in reader:
        tu_dn = i["Symnonyms"]
        tu_dn = [tu_dn]
        for i in tu_dn:
            try: 
                vie_sym = GGtrans(i)
            except:
                vie_sym = "can't translate"
            vie_sym = [vie_sym]
            sym_list.append(vie_sym)
            time.sleep(60/50)

for i in sym_list:
    writer.writerow(i)
            
#             sym_list.append(i["Symnonyms"])
# print(sym_list)