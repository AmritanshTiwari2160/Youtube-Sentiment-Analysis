import csv
from googletrans import Translator

def translate_csv(input_file, output_file):
  """
  Reads a CSV file, translates non-English cells to English
  (focusing on Hindi), and stores the translated content in a new CSV file.
  Skips lines with cells not in Hindi or English.

  Args:
      input_file (str): Path to the input CSV file.
      output_file (str): Path to the output CSV file.
  """

  translator = Translator()
  translated_data = []

  try:
    # Open input file in read mode
    with open(input_file, 'r', encoding='utf-8') as csvfile:
      reader = csv.reader(csvfile)
      count=1
      trans=0
      # Read and translate data, filtering by language
      for row in reader:
        translated_row = []
        count+=1
        for cell in row:
          try:
            print(count)
            # Detect language using Google Translate (heuristic approach)
            detected_lang = translator.detect(cell).lang

            if detected_lang != 'en':  # Translate cells that are not in English
              translated_text = translator.translate(cell, dest='en').text
              translated_row.append(translated_text)
              trans+=1
            else:
              translated_row.append(cell)

          except Exception as e:  # Handle potential translation errors gracefully
            print(f"Error translating cell: {e}")
            translated_row.append(cell)  # Fallback: keep original cell

        # Only append translated rows if the loop completed (not skipped)
        if translated_row:
          translated_data.append(translated_row)

    # Create a new output file in write mode
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
      writer = csv.writer(outfile)
      writer.writerows(translated_data)

    print(f"CSV file translated successfully! Output: {output_file}")
    print("Number of translated lines: " ,trans)
    
  except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")

if __name__ == '__main__':
  input_file = input("Input File name and address: ")  # Enter your input file path and name
  output_file = input("Output File name and address: ")  # Enter your output file path and name

  translate_csv(input_file, output_file)
