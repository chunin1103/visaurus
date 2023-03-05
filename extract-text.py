import csv
from google_translate2 import GGtrans

# open the file in the write mode
f = open('all30k.csv', 'w', encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(f)

# open Vietnamese text file
# with open('30k.txt', encoding='utf8') as f:
with open('adding_words.csv', encoding='utf-8') as f:
    lines = f.readlines()

# Extract each line with @ to get word into word list
word_list = []
# n = 82568 Vietnamese words in this dictionary
for line in lines:
    # if "@" in line:
    # Get all Vietnamese words in the dict
    line = line.strip()
    line = line.replace("@", "")
    line = [line]
    # Translate to English
    line_eng = GGtrans(line[0])
    line.append(line_eng)
    # Checking if a word is Capitalized or not
    if any(letter.isupper() for letter in line[0]):
        line.append("isSuper")
    

# print(line, end = "")
    word_list.append(line)


        
print(word_list)
for i in word_list:
    writer.writerow(i)


# close the file
f.close()