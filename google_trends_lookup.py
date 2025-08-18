# google_trends_lookup.py
import pandas as pd
from pytrends.request import TrendReq
from trend_extractor import load_all_data, calculate_trends
import time
import os

pytrends = TrendReq(hl="en-US", tz=360)

def fetch_trend_data(keyword):
    """Henter Google Trends-data for ett nøkkelord"""
    try:
        pytrends.build_payload([keyword], timeframe="today 12-m")
        df = pytrends.interest_over_time()
        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])
        df = df.rename(columns={keyword: keyword.replace(" ", "_")})
        return df
    except Exception as e:
        print(f"Feil ved søk på {keyword}: {e}")
        return None

if __name__ == "__main__":
    print("🔍 Leser trender fra nyhets- og reddit-data ...")
    all_data = load_all_data()
    trends = calculate_trends(all_data)

    top_keywords = [word for word, *_ in trends[:10]]
    print(f"\n📈 Henter Google Trends for: {top_keywords}")

    os.makedirs("data", exist_ok=True)
    combined_df = None

    for keyword in top_keywords:
        df = fetch_trend_data(keyword)
        if df is not None:
            if combined_df is None:
                combined_df = df
            else:
                combined_df = combined_df.join(df, how="outer")
        time.sleep(1)  # unngå rate-limiting

    if combined_df is not None:
        combined_df.to_csv("data/trend_keywords.csv")
        print("\n✅ Lagret til: data/trend_keywords.csv")
    else:
        print("\n⚠️ Ingen data ble lagret.")
