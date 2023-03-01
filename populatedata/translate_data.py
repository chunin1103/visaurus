import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("output.csv")

# Create an empty list to store the words
words = []
n = 0
# Loop over the rows in the DataFrame
for index, row in df.iterrows():
    if n<3:
        # Split the response string by comma delimiter and remove the square brackets and quotes
        response = row["Response"].replace("[", "").replace("]", "").replace("'", "")
        print(response)
        words.extend(response.split(", "))
        print(words)
        n+=1
# Convert the list of words to a DataFrame
word_df = pd.DataFrame(words, columns=["Words"])

# Save the DataFrame to a new Excel file
# word_df.to_excel("words.xlsx", index=False)