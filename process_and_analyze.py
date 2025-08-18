from data_collector.reddit_scraper import get_reddit_posts
from data_collector.news_scraper import get_latest_news
from data_collector.save_data import save_to_json
from analysis.sentiment import simple_sentiment

def simple_sentiment(text):
    """Very basic sentiment check."""
    text = text.lower()
    if any(word in text for word in ["good", "great", "success", "positive", "win"]):
        return "Positive"
    elif any(word in text for word in ["bad", "fail", "negative", "loss", "problem"]):
        return "Negative"
    return "Neutral"

def run_analysis():
    # Reddit data
    print("=== Fetching Reddit posts ===")
    reddit_data = get_reddit_posts(subreddit="technology", limit=3)
    for post in reddit_data:
        print(f"\n--- Reddit Post ---")
        print(f"Title: {post['title']}")
        print(f"Sentiment: {simple_sentiment(post['title'])}")
        print(f"URL: {post['url']}")

    # News data
    print("\n=== Fetching News Articles ===")
    news_data = get_latest_news(topic="AI", limit=3)
    for article in news_data:
        print(f"\n--- News Article ---")
        print(f"Title: {article['title']}")
        print(f"Summary: {article['description'] or 'No description available'}")
        print(f"URL: {article['url']}")

    # Lagre begge datasett
    save_to_json(reddit_data, "data/reddit_data.json")
    save_to_json(news_data, "data/news_data.json")

if __name__ == "__main__":
    run_analysis()