import matplotlib.pyplot as plt
import polars as pl
import pandas as pd

def get_mean(df):
    mean = df.select("median_house_value").drop_nulls().mean()
    return mean

def get_median(df):
    median = df.select("median_house_value").drop_nulls().median()
    return median

def get_sd(df):
    sd = df.select("median_house_value").drop_nulls().std()
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

    
