import pandas as pd

# Specify the path to the CSV file
csv_file_path = '/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined2.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Check if the 'CODE_x' column exists in the DataFrame
if 'CODE' in df.columns:
    # Rename the 'CODE_x' column to 'CODE'
    df.rename(columns={'REASONCODE': 'MEDICATIONS_REASONCODE'}, inplace=True)

# Save the modified DataFrame back to a new CSV file
output_csv_file = '/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined2.csv'
df.to_csv(output_csv_file, index=False)