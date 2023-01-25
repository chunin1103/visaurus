import pandas as pd

# Declare all columns
col_list = ["Từ gốc","Từ dịch", "In hoa?","Symnonym","Từ đồng nghĩa","Symnonym_Onelook", "Từ đồng nghĩa Onelook", "Globse"]
df = pd.read_csv("82k.csv", encoding="utf8", usecols=col_list)

# Convert the columns to string type
df['Symnonym_Onelook'] = df['Symnonym_Onelook'].astype(str)
df['Từ đồng nghĩa Onelook'] = df['Từ đồng nghĩa Onelook'].astype(str)


# Create a new column to store the original words that haven't been translated
df['untranslated_words'] = None

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    original_words_list = [word.strip() for word in row['Symnonym_Onelook'].split(',')]
    translated_words_list = [word.strip() for word in row['Từ đồng nghĩa Onelook'].split(',')]    
    translated_words = []

    for translated_word in translated_words_list:
        if translated_word not in original_words_list:
            translated_words.append(translated_word)
    # If there are untranslated words, store them in the "untranslated_words" column
    if translated_words:
        df.at[index, 'translated_words'] = ','.join(translated_words)


# Save the updated DataFrame to a new CSV file
df.to_csv('updated_file2.csv', encoding="utf8", index=False)