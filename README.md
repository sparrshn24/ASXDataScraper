# Script Readme

This Python script is designed to scrape data from the "ASX" subreddit using the Reddit API and the PRAW library. It retrieves information about the latest posts in the subreddit and saves the data in a structured format.

## Prerequisites
- Python 3.x
- PRAW library (`pip install praw`)

## Getting Started
1. Install the required dependencies by running `pip install praw` in your command line.
2. Replace the placeholders in the script with your own Reddit API credentials:
   - `client_id`: Your Reddit client ID
   - `client_secret`: Your Reddit client secret
   - `password`: Your Reddit account password
   - `user_agent`: A descriptive user agent string
   - `username`: Your Reddit username
3. Run the script using Python.

## Script Overview
1. The script imports the necessary modules and libraries.
2. It authenticates with the Reddit API using the provided credentials.
3. The script defines the target subreddit as "ASX" (Australian Securities Exchange).
4. Two functions are defined to retrieve and process the post data:
   - `getPostAsDict(post)`: Takes a Reddit post object and returns a dictionary containing relevant information about the post, such as subreddit, URL, subtext, title, ID, response, upvote ratio, and time.
   - `getResponse(post)`: Takes a Reddit post object and retrieves the response text from comments associated with the post.
5. The script sets the desired date range for data retrieval. In this example, it retrieves all posts from the current time until a specified date (`req_date`).
6. It iterates over the new posts in the "ASX" subreddit and calls `getPostAsDict()` to get the post data.
7. The script saves the post data to a specific path based on the post's timestamp.
8. The script prints the post dictionary for each post retrieved.

Note: The script assumes the existence of a custom module called "comments" that contains additional code. Please ensure the proper import and functionality of this module for the script to work correctly.

Feel free to modify the script according to your specific requirements or add additional functionality as needed.
