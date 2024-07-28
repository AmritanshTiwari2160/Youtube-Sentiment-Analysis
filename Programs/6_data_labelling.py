import csv
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

def label_comments(input_file, output_file):
    # Initialize the VADER SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r', encoding='utf-8') as csvfile, open(output_file, 'w', newline='', encoding='utf-8') as outcsv:
        reader = csv.reader(csvfile)
        writer = csv.writer(outcsv)
        
        # Write the header to the output CSV file
        writer.writerow(['text', 'label'])

        # Iterate through each row in the input CSV file
        for row_number, row in enumerate(reader, start=1):
            # Skip empty lines
            if not row:
                print(f"Skipping empty line at row {row_number}")
                continue
            
            # Skip invalid lines
            if len(row) < 1:
                print(f"Skipping invalid line at row {row_number}: {row}")
                continue
            
            text = row[0]  # Extract the comment text from the row
            sentiment = sia.polarity_scores(text)['compound']  # Get the sentiment score

            # Determine the sentiment label based on the sentiment score
            if sentiment >= 0.05:
                label = 1  # Positive
            elif sentiment <= -0.05:
                label = 0  # Negative
            else:
                label = 2  # Neutral
            
            # Write the comment text and its sentiment label to the output CSV file
            writer.writerow([text, label])

# Run the label_comments function with the specified input and output files
input_file=input("Path and Name of Input File: ")
output_file=input("Path and Name of Output File: ")
label_comments(input_file,output_file)
