import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

# Set your YouTube Data API key
API_KEY = "Your_API_Key"

# Set the YouTube video ID
VIDEO_ID = "Youtube_Video_ID"

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Initialize variables
total_comments_fetched = 0
comments = set()  # Use a set to store comments to avoid duplicates

# Function to fetch comments
def fetch_comments(youtube, video_id, next_page_token=None):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        order="relevance",  # Sort by top comments
        maxResults=100,  # Fetch only 100 comments per request
        textFormat="plainText",
        pageToken=next_page_token
    )
    return request.execute()

# Fetch comments loop
next_page_token = None
while total_comments_fetched < 10000:  # Adjust the limit as needed
    try:
        response = fetch_comments(youtube, VIDEO_ID, next_page_token)
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            # Add comment to the set (sets automatically handle duplicates)
            if comment not in comments:
                comments.add(comment)
                total_comments_fetched += 1
                print(total_comments_fetched)

        # Check if there is a next page token
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    except HttpError as error:
        # Handle quota errors (or any other API errors)
        if error.resp.status in [429, 500, 502, 503, 504]:
            print(f"Quota limit reached or API error: {error}")
            time.sleep(10)  # Wait for 10 seconds before retrying
            continue  # Retry the same request
        else:
            raise  # Raise the exception for other errors

print(f"Fetched {total_comments_fetched} unique comments.")

# Write comments to CSV
csv_file = "file_path_and_name.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows([[comment] for comment in comments])

print(f"Comments saved to '{csv_file}'")