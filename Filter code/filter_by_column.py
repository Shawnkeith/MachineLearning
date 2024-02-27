import csv

# Specify the path to the first CSV file (source)
source_csv_file = '/Volumes/ML Data/synthea_1m_fhir_3_0_May_24/output_1/csv/patients.csv'

# Specify the path to the second CSV file (destination)
destination_csv_file = '/Users/shawngoforth/Desktop/Intro to ML/Final-Project/CombinedData/combined1.csv'

# Columns to extract from the source CSV (0-based index)
source_column_index = 5

# Open the source CSV file for reading with the appropriate encoding
with open(source_csv_file, 'r', encoding='utf-8') as source_csv_input_file:
    # Create a CSV reader with ',' as the delimiter
    source_csv_reader = csv.reader(source_csv_input_file, delimiter=',')

    # Create a dictionary to store the values from the source CSV
    source_data = {}

    # Iterate through rows in the source CSV
    for row in source_csv_reader:
        if len(row) > source_column_index:
            source_data[row[0]] = row[source_column_index]

# Open the destination CSV file for reading and writing with the appropriate encoding
with open(destination_csv_file, 'r', encoding='utf-8') as dest_csv_input_file:
    # Create a CSV reader with ',' as the delimiter for the destination file
    dest_csv_reader = csv.reader(dest_csv_input_file, delimiter=',')

    # Create a list to store the modified data
    modified_data = []

    # Iterate through each row in the destination CSV
    for row in dest_csv_reader:
        if len(row) > 3:
            # Replace the value in column 3 with the corresponding value from the source data
            identifier = row[0]  # Assuming column 0 contains the identifier
            source_value = source_data.get(identifier, 'false')
            if not source_value:
                source_value = 'false'
            row[3] = source_value

        # Append the modified row to the list
        modified_data.append(row)

# Write the modified data to a new CSV file
# Overwrite the destination CSV file with the modified data
with open(destination_csv_file, 'w', newline='', encoding='utf-8') as destination_csv_file:
    # Create a CSV writer with ',' as the delimiter
    dest_csv_writer = csv.writer(destination_csv_file, delimiter=',')

    # Write the modified data to the destination CSV file, overwriting the existing data
    dest_csv_writer.writerows(modified_data)