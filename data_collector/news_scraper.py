import requests
import json
import datetime
import os

API_KEY = "a0512c043ebc476a83c9a24a984c69e7"  # ← Bytt ut med din egen
KEYWORDS = ["blockchain", "AI ethics", "cybersecurity"]
FROM_DATE = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
TO_DATE = datetime.datetime.now().strftime('%Y-%m-%d')

articles = []

for kw in KEYWORDS:
    url = (
        f"https://newsapi.org/v2/everything?q={kw}&from={FROM_DATE}&to={TO_DATE}"
        f"&sortBy=popularity&pageSize=100&language=en&apiKey={API_KEY}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for article in data.get("articles", []):
            articles.append({
                "keyword": kw,
                "title": article["title"],
                "description": article["description"],
                "content": article["content"],
                "publishedAt": article["publishedAt"],
                "source": article["source"]["name"],
                "url": article["url"]
            })
    else:
        print(f"Feil ved søk på {kw}: {response.status_code}")

# Lagre som JSON
os.makedirs("data", exist_ok=True)
with open("data/news_articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"{len(articles)} artikler lagret.")
