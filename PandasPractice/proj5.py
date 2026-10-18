import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")
# to print everything you could do the following
# print(df["Name"].to_string())
# to print multiple fields
# print(df[["Name", "Height", "Weight"]])

print(df)

# selection by row if not index_col = Name
# loc means location by label 
# print(df.loc[0])
