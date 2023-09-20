from lib import get_
import pandas as pd
def test_stats():
  df=pd.read_csv("./california_housing_train.csv")
  assert round(get_mean(df),2) == 207300.91
  assert round(get_median(df),2) == 180400.0
  assert round(get_sd(df),2) == 115983.76
