import requests
import json
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")
KEYWORDS = ["blockchain", "AI ethics", "cybersecurity"]

def get_latest_news(topic=None, limit=5):
    """
    Fetch latest news from NewsAPI and return as a list of dicts.
    If topic is None, use default KEYWORDS.
    """
    from_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    to_date = datetime.datetime.now().strftime('%Y-%m-%d')
    articles = []
    search_terms = [topic] if topic else KEYWORDS

    for kw in search_terms:
        url = (
            f"https://newsapi.org/v2/everything?q={kw}&from={from_date}&to={to_date}"
            f"&sortBy=popularity&pageSize={limit}&language=en&apiKey={API_KEY}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for article in data.get("articles", []):
                articles.append({
                    "keyword": kw,
                    "title": article["title"],
                    "description": article["description"],
                    "content": article.get("content") or "",
                    "publishedAt": article["publishedAt"],
                    "source": article["source"]["name"],
                    "url": article["url"]
                })
        else:
            print(f"Error fetching {kw}: {response.status_code}")

    return articles
