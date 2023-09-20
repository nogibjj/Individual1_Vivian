from lib import get_median,get_mean,get_sd,plot
import matplotlib.pyplot as plt
import polars as pl
import pandas as pd


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
