import pandas as pd

# Declare all columns
col_list = ["Từ gốc","Từ dịch", "In hoa?","Symnonym","Từ đồng nghĩa","Symnonym_Onelook", "Từ đồng nghĩa Onelook", "Globse", "Thesaurus.com", "Onelook", "merged"]
df = pd.read_csv("82k_vi_merged.csv", encoding="utf8", usecols=col_list)

# Convert the columns to string type
df['Từ gốc'] = df['Từ gốc'].astype(str)
df['merged'] = df['merged'].astype(str)

# Create a third column to store additional words
df['New_Words'] = None

merged_words = set(word.strip() for words in df["merged"].str.strip().str.split(',') for word in words)
original_words = set(df["Từ gốc"].str.strip())
new_words = merged_words.difference(original_words)

new_words = list(new_words)
import pandas as pd

# Convert the list of words to a DataFrame
df = pd.DataFrame({'words': new_words})

# Export the DataFrame to an Excel file
df.to_excel('words2.xlsx', index=False)