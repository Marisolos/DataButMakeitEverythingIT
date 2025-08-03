from data_collector.news_scraper import get_latest_news
from data_collector.reddit_scraper import get_reddit_posts

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
    print("\n=== Fetching Reddit posts ===")
    reddit_data = get_reddit_posts(subreddit="technology", limit=3)
    for post in reddit_data:
        print("\n--- Reddit Post ---")
        print(f"Title: {post['title']}")
        print(f"Sentiment: {simple_sentiment(post['title'])}")
        print(f"URL: {post['url']}")

    # News data
    print("\n=== Fetching News Articles ===")
    news_data = get_latest_news(topic="AI", limit=3)
    for article in news_data:
        print("\n--- News Article ---")
        print(f"Title: {article['title']}")
        print(f"Summary: {article['description'] or 'No description available'}")
        print(f"URL: {article['url']}")

if __name__ == "__main__":
    run_analysis()
