import praw

# Initialize Reddit client
reddit = praw.Reddit(
    client_id="eGdOHBW3isOhWNo3ARp7_Q",
    client_secret="IHog9-UPkbTikplMo785FmPTM178kQ",
    user_agent="myBot/0.0.1"
)

# Search for posts with specific title in a subreddit (e.g., r/all or r/IAmA)
print("\n")
subreddit = reddit.subreddit("all")
for submission in subreddit.search("fromSouthKorea", sort="hot", limit=5):
    if not submission.stickied:
        print(f"Title : {submission.title}")
        print(f"Score : {submission.score}")
        print(f"🔗 Link: https://reddit.com{submission.permalink}")
        print("-----------")
print("\n")
