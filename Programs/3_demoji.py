import csv
import emoji
import re

def convert_emojis_to_text(csv_file):
    # Open the CSV file for reading and writing
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)  # Read the CSV data into a list

    # Convert emojis to text in each cell and leave other characters unchanged
    for row_idx, row in enumerate(data):
        for col_idx, cell in enumerate(row):
            # Convert emojis to their textual representation
            text_with_emojis = emoji.demojize(cell)
            # Replace non-alphabetical characters in emoji names with a space
            cleaned_text = re.sub(r'(:[^:]+:)', lambda m: re.sub(r'[^a-zA-Z]', ' ', m.group()), text_with_emojis)
            data[row_idx][col_idx] = cleaned_text

    # Write the modified data back to the CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Example usage
csv_file_path = input("Enter path and name of file: ")
convert_emojis_to_text(csv_file_path)
