# Elisey Voichishin cse113 Study.com
# Machine learning with housing

# Personal notes:
# sudo apt install python3-pandas on portable molotov

import matplotlib.pyplot as plt # someting i htihnk
import csv
import pandas as pd

# function to load data from the csv and process
def load_data(file="House_Prices.csv"):
    # READING A CSV FILE
	# price, sqft 
	try:
		df = pd.read_csv(file)
		df['price'] = pd.to_numeric(df['price'], errors='coerce')
		df['sqft'] = pd.to_numeric(df['sqft'], errors='coerce')
		print("Dataset loaded. Shape: \n", df.shape)
		return df
	except FileNotFoundError as e:
		print(f"File not found! {e}")
	except Exception as e:
		print(f"Error! {e}")

def stats(df):
	print(df.describe())

	plt.figure(figsize=(10,6))
	plt.scatter(df['size'], df['price'], color='pirple', s=50, label="Data Points")
	plt.title("House price vs sqft")
	plt.xlabel("Sqft")
	plt.ylabel("Price")
	plt.grid(True)
	plt.legend()

	# lets save for later too just in case
	plt.savefig("scatter_plot.png", dpi=300, bbox_inches='tight')
	plt.show()


def train_model():
    pass

def predict_price():
    pass

def main():
    load_data()
    pass

main()

# sources
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# https://github.com/ywchiu/riii/blob/master/data/house-prices.csv 
