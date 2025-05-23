import sys
import pandas as pd
from tabulate import tabulate

from src.feature_engineer import compute_stat_difference, add_label_column

df = pd.read_csv("data/processed/testfights.csv")
df = compute_stat_difference(df)
df = add_label_column(df)

important_cols = [
    "fighter_a_name", "fighter_b_name",
    "rank_diff", "last_4_win_diff", "last_4_finish_diff",
    "win_streak_diff", "age_diff", "height_diff", "reach_diff", "winner"
]
# print(df.head())
print(tabulate(df[important_cols], headers="keys", tablefmt="fancy_grid"))
