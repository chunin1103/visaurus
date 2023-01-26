import pandas as pd

# Create data frame
df = pd.DataFrame({
    'Vietnamese Word': ['Tên', 'số', 'sức', 'mạnh', 'người'],
    'Synonyms': ['tên đệm', 'chữ số', 'sức lực', 'cường độ', 'con người']
})

# Create a third column to store additional words
df['New Words'] = None

# Loop through the words in column 2
for i, synonym in enumerate(df['Synonyms']):
    # Split the words in column 2
    syn_words = synonym.split(',')
    # Loop through the split words
    for word in syn_words:
        # Check if the word is in column 1
        if word not in list(df['Vietnamese Word']):
            # If not, add the word to the third column
            df.at[i, 'New Words'] = word

# Print the data frame
print(df)