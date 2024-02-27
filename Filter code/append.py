import pandas as pd

# Specify the path to the source CSV file
df_conditions = pd.read_csv('/Volumes/ML Data/synthea_1m_fhir_3_0_May_24/output_1/csv/observations.csv')

# Specify the path to the second CSV file (destination)
df_combined3 = pd.read_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined1.csv')

# Group the conditions by 'PATIENT' and aggregate the 'CODE' values into a list
conditions_aggregated = df_conditions.groupby('PATIENT')['CODE'].apply(list).reset_index()

# Merge the DataFrames on the 'ID' column from df_combined1 and 'PATIENT' column from the aggregated conditions
df_final = pd.merge(df_combined3, conditions_aggregated, left_on='ID', right_on='PATIENT', how='left')

# Drop the 'PATIENT' column as it is redundant with 'ID'
df_final.drop('PATIENT', axis=1, inplace=True)

# Save the merged DataFrame to a new CSV file
df_final.to_csv('/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined1.csv', index=False)

