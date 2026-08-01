# # Elisey Voichishin cse113 Study.com
# Machine learning with housing

# example data
# Price,SqFt
# 114300,1790
# 114200,2030
# 114800,1740
# 94700,1980
# 119800,2130
# 114600,1780
# 151600,1830
# 150700,2160
# 119200,2110
# 104000,1730
# 132500,2030
# 123000,1870
# 102600,1910
# 126300,2150
# 176800,2590
# 145800,1780
# 147100,2190
# 83600,1990
# 111400,1700
# 167200,1920

"""
Code explanation: Loads housing data from a csv file 
as the above example. It uses scikits- LinearRegression to find the best fit line 
that can predict price via stats based on size. It splits the data
into training and testing sets to check performance using r^2 and rmse metrics
and displays a scatter plot as a png and a regression line. After showing all of that
it enters a loop where user can input sqft to get price estimates. 
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# function to load data from the csv and process, takes file as argument. Default = "House_Prices.csv"
def load_data(file="House_Prices.csv"):
    # READING A CSV FILE
    # price, sqft 
    try:
        df = pd.read_csv(file)
        # Convert to numeric in case of weird formatting
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['SqFt'] = pd.to_numeric(df['SqFt'], errors='coerce')
        print(f"Dataset loaded. Shape: {df.shape}")
        return df
    except FileNotFoundError as e:
        print(f"File not found! {e}")
        return None
    except Exception as e:
        print(f"Error! {e}")
        return None

# function to display statistics and scatter plot, takes dataframe as an argument
def stats(df):
    # Basic stats from pandas
    print("\nDataset Statistics:")
    print(df.describe())

    # Scatter plot to visualize relationship
    plt.figure(figsize=(10,6))
    plt.scatter(df['SqFt'], df['Price'], color='purple', s=50, label="Data Points")
    plt.title("House price vs SqFt")
    plt.xlabel("SqFt")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()

    # save it into a png
    plt.savefig("scatter_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

# train the linear regression model, takes housing data as an argument
def train_model(data):
    # Features (X) and target (y)
    x = data[['SqFt']].values
    y = data['Price'].values

    # Split into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    print(f"\nTraining set: {len(x_train)} samples")
    print(f"Test set: {len(x_test)} samples")
    
    # Create and train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Predictions for both sets
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    # Calculate performance metrics
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    # Display results
    print(f"\nCoefficient: ${model.coef_[0]:,.2f} per sqft")
    print(f"Intercept: ${model.intercept_:,.2f}")
    print(f"R^2 Score in training: {train_r2:.4f}")
    print(f"R^2 Score in test: {test_r2:.4f}")
    print(f"RMSE training: ${train_rmse:,.2f}")
    print(f"RMSE test: ${test_rmse:,.2f}")

    return model, x, y, test_r2

# function to plot regression line, takes data and model as arguments
def plot_regression(data, model):
    # Plot the data points
    plt.figure(figsize=(10,6))
    plt.scatter(data['SqFt'], data['Price'], alpha=0.7, color='blue', label='Data')

    # Create a range of x values and predict y for the regression line
    x_range = np.linspace(data['SqFt'].min(), data['SqFt'].max(), 100).reshape(-1,1)
    y_pred_line = model.predict(x_range)
    plt.plot(x_range, y_pred_line, color='red', linewidth=2, label='Regression Line')
    
    plt.xlabel('House size in sqft')
    plt.ylabel('Price')
    plt.title('Linear Regression: Housing Prices vs Size')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig('housing_regression.png', dpi=150)
    plt.show()

# function to predict price, takes model as an argument
def predict_price(model):
    # Interactive prediction loop
    try:
        while True:
            inp = input("\nEnter house size in sqft or quit to exit: ").strip()
            # Check if user wants to exit
            if inp.lower() in ["quit", 'q', "exit"]:
                print("Exiting...")
                break

            # Convert input to float
            size = float(inp)

            # Validate input
            if size <= 0:
                print("Please enter a positive value.")
                continue

            # Predict using the trained model
            size_reshaped = np.array([[size]])
            predicted_price = model.predict(size_reshaped)[0]

            print(f"\nPredicted price for {size:,.0f} sqft: ${predicted_price:,.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Load the data
    data = load_data("House_Prices.csv")
    
    if data is None:
        print("Could not load data. Exiting.")
        return
    
    # Show statistics and scatter plot
    stats(data)

    # Train the model
    model, x, y, r2 = train_model(data)

    # Show the regression line
    print("\nDisplaying regression line...")
    plot_regression(data, model)

    # Start prediction loop
    predict_price(model)

main()

# Sources
# W3Schools. (2024). Pandas getting started. https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# ywchiu. (2015). riii/data/house-prices.csv [Data file]. GitHub. https://github.com/ywchiu/riii/blob/master/data/house-prices.csv
# DigitalOcean. (2022, August 3). Scikit-learn: A beginner’s guide to machine learning in Python. https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial
# Rabianaz22. (2024). A guide to machine learning with scikit-learn. Kaggle. https://www.kaggle.com/code/rabianaz22/a-guide-to-machine-learning-with-scikit-learn