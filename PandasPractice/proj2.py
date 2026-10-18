# more series
import pandas as pd

calories = {"day 1" : 1750, "day 2" : 2100, "day 3" : 1700}

series = pd.Series(calories)

print(series)
series.loc["day 2"] += 200
print(series.loc["day 2"])


print(series[series >= 2000])
