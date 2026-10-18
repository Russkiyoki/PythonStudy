# data frames
import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
		"Age" : [30,35,50]
}

#D and F capped because its a constructor
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df.loc["Employee 1"])
