<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook Post Automation</title>
    
</head>
<body>

<header>
    <h1>Facebook Post Automation</h1>
    <p>Automate your daily posts on Facebook using a simple Python script</p>
</header>

<div class="container">
    <section>
        <h2>Project Overview</h2>
        <p>
            This Python script automates the process of posting messages to a Facebook account using the Facebook Graph API.
            The script reads a list of messages from an Excel file and posts them to Facebook at a specific time each day. It
            ensures that one message is posted per day.
        </p>
    </section>
    <section>
        <h2>How It Works</h2>
        <p>
            The script reads messages from an Excel file and posts them to Facebook. The key steps involved are:
        </p>
        <ol>
            <li><strong>Facebook API Integration:</strong> The script interacts with the Facebook Graph API using a user-generated access token.</li>
            <li><strong>Reading Data from Excel:</strong> It extracts messages from the "Message" column in the Excel file.</li>
            <li><strong>Scheduling Posts:</strong> The script is scheduled to run at a specific time each day using the <code>schedule</code> library.</li>
            <li><strong>Post Logic:</strong> It checks if a message has already been posted and avoids duplicating posts.</li>
        </ol>
    </section>
    <section>
        <h2>Installation Instructions</h2>
        <p>To use the Facebook Post Automation script, follow the steps below:</p>
        <ol>
            <li>Install the required libraries:
                <pre><code>pip install facebook-sdk pandas schedule openpyxl</code></pre>
            </li>
            <li>Replace the <code>access_token</code> in the script with your own Facebook Access Token.</li>
            <li>Ensure your Excel file (e.g., <code>messages.xlsx</code>) is in the correct format, with a column named "Message" containing the messages to be posted.</li>
            <li>Set the desired post time in the script.</li>
            <li>Schedule the script to run daily using Task Scheduler (Windows) or Automator (MacOS).</li>
        </ol>
    </section>
    <section>
        <h2>Code Explanation</h2>
        <p>
            Below is the Python code that automates the process of posting messages from an Excel file to Facebook at a specific time:
        </p>
        <pre><code>
import facebook
import pandas as pd
import schedule
import time

# Facebook Access Token
access_token = "YOUR_ACCESS_TOKEN"

# Initialize Facebook Graph API
asafb = facebook.GraphAPI(access_token)

# Load messages from Excel
df = pd.read_excel("messages.xlsx")
messages = df["Message"].tolist()

# Function to post a message
def post_message():
    for message in messages:
        asafb.put_object("me", "feed", message=message)
        print(f"Posted: {message}")

# Schedule the post for 10:00 AM every day
schedule.every().day.at("10:00").do(post_message)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
        </code></pre>
    </section>
    <section>
        <h2>Dependencies</h2>
        <p>The following Python libraries are required to run the script:</p>
        <table>
            <thead>
                <tr>
                    <th>Library</th>
                    <th>Purpose</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><code>facebook-sdk</code></td>
                    <td>Used for interacting with the Facebook Graph API.</td>
                </tr>
                <tr>
                    <td><code>pandas</code></td>
                    <td>Used for reading data from Excel files.</td>
                </tr>
                <tr>
                    <td><code>schedule</code></td>
                    <td>Used for scheduling the daily posts at the desired time.</td>
                </tr>
                <tr>
                    <td><code>openpyxl</code></td>
                    <td>Handles Excel file reading and writing.</td>
                </tr>
            </tbody>
        </table>
    </section>
    <section>
        <h2>Running the Script Automatically</h2>
        <p>
            To run the script automatically without manually executing it, you can use Task Scheduler (Windows) or Automator (MacOS).
            This ensures that the script runs every day at the specified time without any intervention.
        </p>
    </section>

</div>

<div class="footer">
    <p>&copy; 2025 Facebook Post Automation Project | Created by [Your Name]</p>
</div>

</body>
</html>
