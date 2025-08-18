from textblob import TextBlob

def simple_sentiment(text):
    """
    Returnerer 'Positive', 'Negative' eller 'Neutral' basert på enkle sentiment-analyse.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"
