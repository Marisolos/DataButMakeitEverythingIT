import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def get_reddit_posts(subreddit="technology", keywords=None, limit=5):
    """
    Fetch Reddit posts from a subreddit containing any of the keywords.
    """
    if keywords is None:
        keywords = ["AI", "security", "privacy", "cloud", "automation", "governance"]

    results = []
    for submission in reddit.subreddit(subreddit).new(limit=100):
        title = submission.title.lower()
        for kw in keywords:
            if kw.lower() in title:
                results.append({
                    "subreddit": subreddit,
                    "keyword": kw,
                    "title": submission.title,
                    "score": submission.score,
                    "url": submission.url,
                    "created_utc": submission.created_utc,
                    "content": getattr(submission, "selftext", "")
                })
                break
        if len(results) >= limit:
            break

    return results
