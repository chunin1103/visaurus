import pandas as pd
import re
import os

# Read CSV file and store in a pandas DataFrame
df = pd.read_csv('words3.csv')

# Select only non-"FALSE" values and non-NaN values in the "Ver1" column
words = df.loc[(df['Ver1'] != 'FALSE') & (df['Ver1'] != False) & (df['Ver1'] == df['Ver1']), 'Ver1'].tolist()

# Exclude words that start with an uppercase letter using regular expression
words = [word for word in words if not re.match(r'^[A-Z]', word)]

# Print the list of Vietnamese words
print(words)

# Export the list of Vietnamese words to an Excel file
df_export = pd.DataFrame({'tu_tieng_Viet': words})
df_export.to_csv('adding_words.csv', index=False, header=True, sep=',', encoding='utf-8')