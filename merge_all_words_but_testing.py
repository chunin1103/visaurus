from collections import Counter
import pandas as pd

# Declare all columns
col_list = ["Tu_goc","Tu_dich", "Thesaurus","Thesaurus_vi","Onelook", "Onelook_vi", "Globse", "Thesaurus_merged", "Onelook_merged", "All merged"]
df = pd.read_csv("10k.csv", encoding="utf-8", usecols=col_list)

# Convert the columns to string type
df['Thesaurus_vi'] = df['Thesaurus_vi'].astype(str)
df['Onelook_vi'] = df['Onelook_vi'].astype(str)
df['Globse'] = df['Globse'].astype(str)

# Merge the columns into one list and remove duplicates
df = df.assign(merged=df.apply(lambda x: ",".join(sorted(list(set(
    [word.strip() for word in str(x["Globse"]).split(",") if pd.notnull(word)] +
    [word.strip() for word in str(x["Thesaurus_vi"]).split(",") if pd.notnull(word) and word.strip() not in set([w.strip() for w in str(x["Thesaurus"]).split(",")])] +
    [word.strip() for word in str(x["Onelook_vi"]).split(",") if pd.notnull(word) and word.strip() not in set([w.strip() for w in str(x["Onelook"]).split(",")])])))),
    axis=1))

# Sort the words in the merged list by their frequency of occurrence in the other columns
def sort_by_frequency(row):
    merged_words = [word.strip() for word in str(row["merged"]).split(",") if pd.notnull(word)]
    other_columns = ["Globse", "Thesaurus_vi", "Onelook_vi"]
    word_counts = Counter()
    for col in other_columns:
        words = [word.strip() for word in str(row[col]).split(",") if pd.notnull(word)]
        word_counts.update(words)
    sorted_words = sorted(merged_words, key=lambda word: word_counts[word], reverse=True)
    return ",".join(sorted_words)

df["all_merged"] = df.apply(sort_by_frequency, axis=1)

# Print the resulting dataframe
print(df)

# Write the resulting dataframe to a CSV file
df.to_csv('updated_file5.csv', encoding="utf-8", index=False)