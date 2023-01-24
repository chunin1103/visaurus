import pandas as pd
col_list = ["Từ gốc","Từ dịch", "In hoa?","Symnonym","Từ đồng nghĩa","Symnonym_Onelook", "Từ đồng nghĩa Onelook", "Globse"]
df = pd.read_csv("82k.csv", encoding="utf8", usecols=col_list)

# Convert the columns to string type
df['Symnonym'] = df['Symnonym'].astype(str)
df['Từ đồng nghĩa'] = df['Từ đồng nghĩa'].astype(str)


# Create a new column to store the original words that haven't been translated
df['untranslated_words'] = None

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    original_words_list = row['Symnonym'].split(',')
    translated_words_list = [word.strip() for word in row['Từ đồng nghĩa'].split(',')]    
    untranslated_words = []

    for original_word in original_words_list:
        original_word = original_word.strip()
        if original_word in translated_words_list:
            untranslated_words.append(original_word)
    # If there are untranslated words, store them in the "untranslated_words" column
    if untranslated_words:
        df.at[index, 'untranslated_words'] = ','.join(untranslated_words)


# Save the updated DataFrame to a new CSV file
df.to_csv('updated_file.csv', index=False)