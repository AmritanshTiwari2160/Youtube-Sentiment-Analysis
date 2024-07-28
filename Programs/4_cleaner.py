import csv
import re

def clean_text(text):
    # Remove all non-alphabetic characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    cleaned_text = cleaned_text.lower()
    # Replace multiple spaces/newlines/tabs with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def clean_csv(input_file, output_file):
    """
    Reads a CSV file, cleans text in each cell, and stores the cleaned data in a new CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file (optional, defaults to 'cleaned.csv').
    """

    cleaned_data = []
    try:
        # Open input file in read mode
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            # Read and clean data
            for row in reader:
                cleaned_row = [clean_text(cell) for cell in row]
                cleaned_data.append(cleaned_row)

        # Write cleaned data to the output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_data)

        print(f"CSV file cleaned successfully! Output: {output_file}.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == '__main__':
    input_file = input("Enter input file path and name: ")  # Replace with your input CSV file path
    output_file = input("Enter output file path and name: ")  # Specify a different output filename (or leave blank to overwrite)
    clean_csv(input_file, output_file)
