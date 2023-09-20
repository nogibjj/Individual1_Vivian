import matplotlib.pyplot as plt
import pandas as pd
# import polars as pl

def get_mean(df):
    mean = df["median_house_value"].dropna().mean()
    return mean

def get_median(df):
    median = df["median_house_value"].dropna().median()
    return median

def get_sd(df):
    sd = df["median_house_value"].dropna().std()
    return sd

def plot(csv):
    # Plot a histogram for the house value
    data = pd.read_csv(csv)['median_house_value'].dropna()

    # Create histogram
    plt.hist(data, bins=5, edgecolor="k")

    # Add labels and title
    plt.xlabel('median_house_value')
    plt.ylabel('Frequency')
    plt.title('Histogram of median house price')

    # Show plot
    plt.show()

    
