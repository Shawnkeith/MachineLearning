import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined2.csv')

# Check if there are at least two columns in the DataFrame
if df.shape[1] >= 2:
    # Remove the last two columns
    df = df.iloc[:, :-1]

    # Save the modified DataFrame back to the CSV file
    df.to_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined2.csv', index=False)

    print("Last two columns removed successfully and saved to 'your_modified_file.csv'.")
else:
    print("Error: DataFrame has fewer than two columns.")