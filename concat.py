import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file = 'test_mask.xlsx'  # Replace 'your_excel_file.xlsx' with the path to your Excel file
column_name = 'file_name'  # Replace 'Column1' with the name of the column you want to modify

df = pd.read_excel(excel_file)

# Concatenate ".mp4" with each value in the specified column
df[column_name] = df[column_name].astype(str) + ".mp4"

# Save the modified DataFrame back to the Excel file
df.to_excel(excel_file, index=False)
