from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

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
    df_final = df_all_together
else:
    print("⚠️ Lite variasjon – henter separat og normaliserer.")
    dataframes = [hent_trend(k, geo=geo, timeframe=timeframe) for k in keywords]
    df_combined = pd.concat(dataframes, axis=1)
    df_final = (df_combined - df_combined.min()) / (df_combined.max() - df_combined.min()) * 100

# Lagre til CSV
df_final.to_csv("data/google_trends.csv")
print("📁 Lagret data til data/google_trends.csv")

# ----------------------------
# Plot resultatet
# ----------------------------
df_final.plot(figsize=(10, 5), title="Google Trends (Normalisert ved behov)")
plt.xlabel("Dato")
plt.ylabel("Interesse (0-100)")
plt.grid(True)
plt.tight_layout()
plt.show()
