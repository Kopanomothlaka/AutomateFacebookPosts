import facebook
import pandas as pd
import schedule
import time
from datetime import datetime

# Facebook Access Token
access_token = "EAAIsylpi9bsBO2a4I6iSVG0IrdZA1oU1mqxxsmSIYHXOhs97AZAZBPjCZCwxMlEMr0zgQkcKsDZA7bZAooXLmFczuFg26vUr9aIwZAeONRYg14sZAEzKmcAA61qZCQZBP2HxVNfeucqHxe8s8Ucy8C63zGSw85cmFzrZA2TduWYtyOzZCCZAKv0tpxrsDarlh23wEVtOas2nZBTDlHLGqLs0KTkG6EZCDfl"

# Initialize the Facebook Graph API
asafb = facebook.GraphAPI(access_token)

# Load messages from Excel
df = pd.read_excel("messages.xlsx")  # Ensure the Excel file is in the same directory
messages = df["Message"].tolist()  # Convert the 'Message' column data to a list

# Fetch recent posts from Facebook
latest_posts = asafb.get_connections("me", "posts")

# Extract existing messages from recent posts
posted_messages = set()
if 'data' in latest_posts:
    for post in latest_posts['data']:
        if 'message' in post:
            posted_messages.add(post['message'])

# Variable to keep track of which message to post
message_index = 0

# Function to post messages
def post_messages():
    global message_index

    if message_index < len(messages):  # Ensure there are messages left to post
        message = messages[message_index]
        
        # Post the message if it hasn't already been posted
        if message not in posted_messages:
            asafb.put_object("me", "feed", message=message)
            print(f"Posted: {message}")
            posted_messages.add(message)
            message_index += 1  # Move to the next message for the next day
        else:
            print(f"Skipped (Already Posted): {message}")
    else:
        print("All messages have been posted.")

# Schedule the task to run every day at 10:00 AM
schedule.every().day.at("10:00").do(post_messages)

# Keep the script running to execute the scheduled task
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute for the next task
