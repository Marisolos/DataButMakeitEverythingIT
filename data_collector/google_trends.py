from pytrends.request import TrendReq

pytrends = TrendReq()
pytrends.build_payload(kw_list=["AI", "blockchain", "cloud computing"], timeframe='today 12-m')

data = pytrends.interest_over_time()
data.to_csv("data/google_trends.csv")
