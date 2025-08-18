import json
import matplotlib.pyplot as plt
from collections import Counter

# Hent Reddit-data
with open("data/reddit_posts.json", "r", encoding="utf-8") as f:
    reddit = json.load(f)

# Hent nyhetsdata
with open("data/news_articles.json", "r", encoding="utf-8") as f:
    news = json.load(f)

# Tell sentiment
reddit_counts = Counter(post["sentiment"] for post in reddit)
news_counts = Counter(article["sentiment"] for article in news)

# Plot Reddit-sentiment
plt.figure(figsize=(8, 4))
plt.bar(reddit_counts.keys(), reddit_counts.values(), color="skyblue")
plt.title("Sentiment i Reddit-poster")
plt.xlabel("Sentiment")
plt.ylabel("Antall")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Plot nyhets-sentiment
plt.figure(figsize=(8, 4))
plt.bar(news_counts.keys(), news_counts.values(), color="salmon")
plt.title("Sentiment i nyhetsartikler")
plt.xlabel("Sentiment")
plt.ylabel("Antall")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
