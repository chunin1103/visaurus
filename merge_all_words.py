import pandas as pd

# Declare all columns
col_list = ["Tu_goc","Tu_dich", "Thesaurus","Thesaurus_vi","Onelook", "Onelook_vi", "Globse", "Thesaurus_merged", "Onelook_merged", "All merged"]
df = pd.read_csv("10k.csv", encoding="utf8", usecols=col_list)

# Convert the columns to string type
df['Thesaurus_vi'] = df['Thesaurus_vi'].astype(str)
df['Onelook_vi'] = df['Onelook_vi'].astype(str)
df['Globse'] = df['Globse'].astype(str)


# Strip words in each column
df["Thesaurus_vi"] = df["Thesaurus_vi"].str.strip()
df["Onelook_vi"] = df["Onelook_vi"].str.strip()
df["Globse"] = df["Globse"].str.strip()

# Merge the columns into one list and remove duplicates
df = df.assign(merged=df.apply(lambda x: ",".join(list(set(
    [word.strip() for word in str(x["Globse"]).split(",") if pd.notnull(word)] +
    [word.strip() for word in str(x["Thesaurus_vi"]).split(",") if pd.notnull(word) and word.strip() not in set([w.strip() for w in str(x["Thesaurus"]).split(",")])] +
    [word.strip() for word in str(x["Onelook_vi"]).split(",") if pd.notnull(word) and word.strip() not in set([w.strip() for w in str(x["Onelook"]).split(",")])]))),
    axis=1))

# Create a new column with a count of each word in the other columns
df["word_count"] = df.apply(lambda x: sum([
    x[col].count(word) if isinstance(x[col], str) else 0 
    for col in ["Globse", "Thesaurus", "Thesaurus_vi", "Onelook", "Onelook_vi"] 
    for word in x["merged"].split(",")
]), axis=1)


# Sort the DataFrame by the word_count column
df = df.sort_values(by=["word_count"], ascending=False)

# Print the resulting dataframe
print(df)

# This will strip any extra whitespaces and convert all words to uppercase before merging and checking for duplicates.
df.to_csv('updated_file4.csv', encoding="utf-8", index=False)



