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

def f(csv):
    #dataset:"california_housing_train.csv"
    df = pl.read_csv(csv)

    print(df.shape)
    print(len(df))
    print(df.describe())

    # Bottom 3 house price
    sorted_by_value = df.sort("median_house_value").limit(3)
    # Calculate the median/mean/standard deviation for the 2022 numbers
    median = get_median(df)
    mean = get_mean(df)
    sd = get_sd(df)
    print("Bottom 3 house price:")
    print(sorted_by_value)
    print("median is: " + str(median))
    print("mean is: " + str(mean))
    print("standard deviation is: " + str(sd))
    plot(csv)


if __name__ == "__main__":
    f("california_housing_train.csv")
    
