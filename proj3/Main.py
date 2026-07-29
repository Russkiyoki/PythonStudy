# Elisey Voichishin cse113 Study.com
# Machine learning with housing

# Personal notes:
# sudo apt install python3-pandas on portable molotov

import matplotlib # someting i htihnk
import csv
import pandas as pd

# function to load data from the csv and process
def load_data():
    # READING A CSV FILE
    with open("House_Prices.csv", "rt") as f:
        data = csv.reader(f)
        for row in data:
            print(row)
    

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