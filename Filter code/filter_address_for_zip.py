import pandas as pd

# Replace 'your_input_file.csv' with the actual file name
input_file = '/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined3.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(input_file)

# Check if the column 'OBSERVATIONS_CODE' exists before removing
if 'OBSERVATIONS_CODE' in df.columns:
    # Remove the 'OBSERVATIONS_CODE' column
    df.drop(columns=['OBSERVATIONS_CODE'], inplace=True)

    # Replace 'your_output_file.csv' with the desired output file name
    output_file = '/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined3.csv'

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Column 'OBSERVATIONS_CODE' removed. Updated data saved to {output_file}")
else:
    print("Column 'OBSERVATIONS_CODE' not found in the CSV file.")
