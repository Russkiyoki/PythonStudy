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

	# save it into a png
	plt.savefig("scatter_plot.png", dpi=300, bbox_inches='tight')
	plt.show()

# train the linear regression model with the housing data
def train_model(data):
	x = data[['Size (sqft)']].values
	y = data['Price'].values

	x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
	print(f"\n Training set: {len(x_train)} samples")
	print(f"Test set: {len(x_test)} samples")
	
	model = LinearRegression()
	model.fit(x_train, y_train)

	y_train_pred = model.predict(x_train)
	y_test_pred = model.predict(x_test)

	train_r2 = r2_score(y_train, y_train_pred)
	test_r2 = r2_score(y_test, y_test_pred)
	train_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred)

	print(f"\n Coefficient: ${model.coef_[0],.2f} per sqft")
	print(f"intercept: ${model.intercept_:,.2f}")
	print(f"Score in training: {train_r2:.4f}")
	print(f"Score in test: {test_r2:.4f}")
	print(f"rmse training: ${train_rmse:,.2f}")
	print(f"rmse test: ${test_rmse:,.2f}")

	return model, x, y, test_r2

def plot_regression(data, model):
	plt.figure(figsize=(10,6)
	plt.scatter(data['size sqft'], data['price'], alpha = 0.7, color = 'blue', label='data')

	x_range = np.linspace(data['size sqft'].min(), data['size sqft'].max(), 100).reshape(-1,1)
	y_pred_line = model.predict(x_range)
	
	plt.xlabel('house size in sqft')
	plt.ylabel('price')
	plt.title('linear regression: Housing Prices vs Size')
	plt.grid(True, alpha=0.3)
	plt.legend()
	plt.savefig('housing_regression.png', dpi=150)
	plt.show()

def predict_price():
	try:
		while True:
			inp = input("\nEnter house size in sqft or quit to exit: ").strip() # to get rid of \n or whatever
			if inp.lower() in ["quit", 'q', "exit"]:
				print("Exiting...")
				break

			size = float(inp)

			if size <= 0:
				print("please enter a positive value.")
				continue

			size_reshaped = np.array([[size]])
			predicted_price = model.predict(size_reshaped)[0]

			print(f"\nPredicted price for {size:,.0f} sqft: ${predicted_price:,.2f}")

	except ValueError:
		print("Invalid input. Please enter a numeric value.")
	except Exception as e:
		print(f"An error occurred: {e}")

def main():
    data = load_data("House_Prices.csv")
	
	stats(data)

	print("\ndisplaying data visualization...")
	plot_data(data, save=True)

	model, x, y, r2= train_model(data)

	print(\nDisplaying regression line...")
	plot_regression(data, model)

	predict_price(model)
	pass

main()

# sources
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# https://github.com/ywchiu/riii/blob/master/data/house-prices.csv 
