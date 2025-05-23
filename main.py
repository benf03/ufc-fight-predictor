import sys
import pandas as pd

from src.feature_engineer import compute_stat_difference, add_label_column

df = pd.read_csv("data/processed/testfights.csv")
df = compute_stat_difference(df)
df = add_label_column(df)

print(df.head())
