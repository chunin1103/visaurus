import pandas as pd

# Declare all columns
col_list = ["Từ gốc","Từ dịch", "In hoa?","Symnonym","Từ đồng nghĩa","Symnonym_Onelook", "Từ đồng nghĩa Onelook", "Globse", "Thesaurus.com", "Onelook"]
df = pd.read_csv("82k_vi.csv", encoding="utf8", usecols=col_list)

# Convert the columns to string type
df['Thesaurus.com'] = df['Thesaurus.com'].astype(str)
df['Onelook'] = df['Onelook'].astype(str)
df['Globse'] = df['Globse'].astype(str)


# Strip and uppercase words in each column
df["Thesaurus.com"] = df["Thesaurus.com"].str.strip()
df["Onelook"] = df["Onelook"].str.strip()
df["Globse"] = df["Globse"].str.strip()

# Merge the columns into one list and remove duplicates
df = df.assign(merged = df[["Globse", "Thesaurus.com", "Onelook"]].apply(lambda x: ",".join(list(set(",".join(x).split(",")))), axis =1))

# Print the resulting dataframe
print(df)

# This will strip any extra whitespaces and convert all words to uppercase before merging and checking for duplicates.
df.to_csv('updated_file3.csv', encoding="utf8", index=False)



