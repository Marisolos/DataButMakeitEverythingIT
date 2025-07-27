import praw
import json
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"))

subreddits = ["technology", "MachineLearning", "ITCareerQuestions", "IT", "programming", "datascience", "cscareerquestions", "softwareengineering", "webdev", "learnprogramming"]
keywords = ["AI", "security", "privacy", "cloud", "automation", "governance"]

results = []

for sub in subreddits:
    print(f"Søker i r/{sub}...")
    for submission in reddit.subreddit(sub).new(limit=100):
        title = submission.title.lower()
        for kw in keywords:
            if kw.lower() in title:
                results.append({
                    "subreddit": sub,
                    "keyword": kw,
                    "title": submission.title,
                    "score": submission.score,
                    "url": submission.url,
                    "created_utc": submission.created_utc
                })
                break

# Lagre som JSON
os.makedirs("data", exist_ok=True)
with open("data/reddit_posts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"{len(results)} relevante Reddit-poster lagret.")
