import csv
from encodings import utf_8
from crawl_glosbe_sym import *

# open the file in the write mode
f = open('symnonyms_glosbe.csv', 'w', encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(f)


eng_word_list =[]
with open('all30k.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        eng_word_list.append(row['tu_tieng_Anh'])

eng_sym_list =[]
n=0
m=0
for eng_word in eng_word_list:
    n+=1
    if n<12:
        eng_word = eng_word.replace("a ", "")
        eng_word = eng_word.replace("A ", "")
        eng_word = eng_word.replace("the ", "")
        eng_word = eng_word.replace("The ", "")
        try:
            symnonym_word = get_glosbe(eng_word)
        # to handle sometimes calling gets blocked
        except:
            symnonym_word = ["cannot found"]
            m += 1
            if m == 7:
                wait = input("crashed, press Enter to continue.")
        else:
            m = 0
        print(eng_word)
        eng_word = [eng_word]
        eng_word.append(symnonym_word)
        eng_sym_list.append(eng_word)
        writer.writerow(eng_word)

f.close()