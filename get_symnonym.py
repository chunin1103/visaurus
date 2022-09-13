import csv
from encodings import utf_8
from crawl_data_thesaurus_official import *

# open the file in the write mode
f = open('symnonyms_eng.csv', 'w', encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(f)


eng_word_list =[]
with open('all30k-Vitoen.csv', encoding='utf_8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        eng_word_list.append(row['a'])

eng_sym_list =[]

for eng_word in eng_word_list:
    print(eng_word)
    eng_word = eng_word.replace("a ", "")
    eng_word = eng_word.replace("A ", "")
    eng_word = eng_word.replace("the ", "")
    eng_word = eng_word.replace("The ", "")
    try:
        symnonym_word = crawlThesaurus(eng_word)
    except:
        symnonym_word = ["cannot found"]
    eng_word = [eng_word]
    eng_word.append(symnonym_word[0])
    eng_sym_list.append(eng_word)

for i in eng_sym_list:
    writer.writerow(i)

f.close()