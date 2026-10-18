import pandas as pd

# Series are a 1 dimensional labeled array 

data = [100, 102, 104]

# constructor, not function since the S is capped
# series can get customized index numbers using
# Series(data, index = ["a","b",...])
series = pd.Series(data, index = ["a", "b", "c"])
series.loc["c"] = 200

# for variable look up
print(series.loc["c"])
# for integer location
print(series.iloc[1])

print(series[series >= 200])
