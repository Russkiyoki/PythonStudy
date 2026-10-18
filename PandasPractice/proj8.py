# data cleanimg
import pandas as pd


df = pd.read_csv("pokemon.csv")

# drop irrelavant columns

#df = df.drop(columns=["Legendary", "No"])


#  handling missing data

#df = df.dropna(subset=["Type2"])
# to replace NaN with something else
df = df.fillna({"Type2" : "None"})

# standardize text
df["Name"] = df["Name"].str.lower()


#fix data types
df["Legendary"] = df["Legendary"].astype(bool)

# dropping duplicates
df = df.drop_duplicates()

print(df.to_string())
