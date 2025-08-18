# trend_extractor.py
import os
import json
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from datetime import datetime

# Last ned nødvendige NLTK-ressurser
nltk.download("punkt")
nltk.download("stopwords")

DATA_DIR = "data"
STOPWORDS = set(stopwords.words("english"))

def load_all_data():
    """Leser alle JSON-filer fra data/ og returnerer som liste av dicts"""
    all_data = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            with open(os.path.join(DATA_DIR, file), "r", encoding="utf-8") as f:
                all_data.extend(json.load(f))
    return all_data

def extract_keywords(text):
    """Tokeniserer, fjerner stopwords og ikke-bokstavlige tokens"""
    tokens = word_tokenize(text.lower())
    words = [w for w in tokens if w.isalpha() and w not in STOPWORDS]
    return words

def calculate_trends(data):
    """Beregner frekvens og trend score"""
    df = pd.DataFrame(data)
    if "publishedAt" in df.columns:
        df["date"] = pd.to_datetime(df["publishedAt"], errors="coerce")
    elif "created_utc" in df.columns:
        df["date"] = pd.to_datetime(df["created_utc"], unit="s", errors="coerce")
    else:
        df["date"] = pd.Timestamp(datetime.now())

    df = df.dropna(subset=["date"])

    # Legg til uke-kolonne
    df["week"] = df["date"].dt.to_period("W")

    weekly_counts = {}
    for week, group in df.groupby("week"):
        text = " ".join(str(t) for t in group.get("title", []) + group.get("content", []))
        words = extract_keywords(text)
        weekly_counts[str(week)] = Counter(words)

    # Beregn trend score (siste uke vs snitt av tidligere uker)
    if len(weekly_counts) < 2:
        return []

    all_weeks = sorted(weekly_counts.keys())
    last_week = all_weeks[-1]
    prev_weeks = all_weeks[:-1]

    last_counts = weekly_counts[last_week]
    prev_counts = Counter()
    for w in prev_weeks:
        prev_counts += weekly_counts[w]

    trends = []
    for word, last_freq in last_counts.items():
        prev_avg = prev_counts[word] / max(1, len(prev_weeks))
        if prev_avg > 0:
            trend_score = ((last_freq - prev_avg) / prev_avg) * 100
            if trend_score > 50:  # Kun store hopp
                trends.append((word, trend_score, last_freq, prev_avg))

    trends.sort(key=lambda x: x[1], reverse=True)
    return trends

if __name__ == "__main__":
    data = load_all_data()
    trends = calculate_trends(data)

    print("\n=== Emerging Trends ===")
    for word, score, last_freq, prev_avg in trends[:20]:
        print(f"{word}: {score:.1f}%  (last week: {last_freq}, avg before: {prev_avg:.1f})")
