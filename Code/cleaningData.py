import pandas as pd

# Load the data
file_path = 'Cleaned_Electric_Vehicle_Population_Data.csv'
data = pd.read_csv(file_path)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing Values in Each Column:")
print(missing_values)

# Check for duplicates
duplicates = data.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# If you want to display the duplicate rows, uncomment the following lines
duplicate_rows = data[data.duplicated()]
print("\nDuplicate Rows:")
print(duplicate_rows)

# Save the cleaned data to a new CSV file
cleaned_file_path = 'Cleaned_Electric_Vehicle_Population_Data.csv'
print(f"\nCleaned data saved to {cleaned_file_path}")
