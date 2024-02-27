import pandas as pd

# Read the original CSV file
df_original = pd.read_csv('/Volumes/ML Data/synthea_1m_fhir_3_0_May_24/output_1/csv/observations.csv')
df_original.columns = df_original.columns.str.upper()

# Check if 'DESCRIPTION' and 'CODE' columns exist in the DataFrame
if 'DESCRIPTION' in df_original.columns and 'CODE' in df_original.columns:
    
    df_body_weight = df_original[(df_original['DESCRIPTION'] == 'Diastolic Blood Pressure') & (df_original['CODE'] == '8462-4')]

    # Check if the resulting DataFrame is not empty
    if not df_body_weight.empty:
        # Create a new DataFrame for the desired format
        df_result = pd.DataFrame({
            'ID': df_body_weight['PATIENT'].unique(),
            'DIASTOLIC_BP': df_body_weight.groupby('PATIENT')['VALUE'].last()  # Assuming you want the last value if there are multiple entries
        })

        # Merge with additional information
        df_additional_info = pd.read_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined1.csv')  # Replace 'your_additional_info.csv' with the actual file name

        # Check if 'ID' column exists in the additional information DataFrame
        if 'ID' in df_additional_info.columns:
            df_final_result = pd.merge(df_additional_info, df_result, on='ID')

            # Save the final result to a new CSV file
            df_final_result.to_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined1.csv', index=False)
        else:
            print("Error: 'ID' column not found in the additional information DataFrame.")
    else:
        print("Error: No data found for the specified conditions.")
else:
    print("Error: 'DESCRIPTION' or 'CODE' columns not found in the original DataFrame.")

