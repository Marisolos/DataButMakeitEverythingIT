from pytrends.request import TrendReq
import pandas as pd

# ----------------------------
# Funksjon for å hente trend for ett søkeord
# ----------------------------
def hent_trend(sok, geo="", timeframe="today 5-y"):
    pytrends = TrendReq(hl="en-US", tz=360)
    pytrends.build_payload([sok], timeframe=timeframe, geo=geo)
    df = pytrends.interest_over_time()
    if "isPartial" in df.columns:
        df = df.drop(columns=["isPartial"])
    return df.rename(columns={sok: sok})

# ----------------------------
# Hovedlogikk
# ----------------------------
keywords = ["AI", "Blockchain technology", "Cloud services"]
geo = ""  # Sett til "NO" hvis du vil ha Norge
timeframe = "today 5-y"

pytrends = TrendReq(hl="en-US", tz=360)
pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
df_all_together = pytrends.interest_over_time()

if "isPartial" in df_all_together.columns:
    df_all_together = df_all_together.drop(columns=["isPartial"])

# Sjekk variasjon (std > 0)
variations = df_all_together.std()
if all(variations > 0):
    print("✅ Variasjon funnet – bruker samlet søk.")
    df_all_together.to_csv("data/google_trends.csv")
else:
    print("⚠️ Lite variasjon – henter separat og normaliserer.")
    dataframes = [hent_trend(k, geo=geo, timeframe=timeframe) for k in keywords]
    df_combined = pd.concat(dataframes, axis=1)
    df_normalized = (df_combined - df_combined.min()) / (df_combined.max() - df_combined.min()) * 100
    df_normalized.to_csv("data/google_trends.csv")

print("📁 Lagret data til data/google_trends.csv")
