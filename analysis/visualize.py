import pandas as pd
import matplotlib.pyplot as plt

# Les data
df = pd.read_csv("data/google_trends.csv", parse_dates=["date"], index_col="date")

# Dropp "isPartial"-kolonnen hvis den finnes
if "isPartial" in df.columns:
    df = df.drop(columns=["isPartial"])

# Plot
df.plot(figsize=(10, 5), title="Google Trends: Teknologitrender")
plt.xlabel("Dato")
plt.ylabel("Interesse (0-100)")
plt.grid(True)
plt.tight_layout()
plt.show()
