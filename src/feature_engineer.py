# src/feature_engineer.py

import pandas as pd

def compute_stat_difference(df):
    """
    Compute differencs in key stats between Fighter A and Fighter B.
    For example: reach_diff = A_reach - B_reach
    """
    df["age_diff"] = df["fighter_a_age"] - df["fighter_b_reach"]
    df["height_diff"] = df["fighter_a_height"] - df["fighter_b_height"]
    df["reach_diff"] = df["fighter_a_reach"] - df["fighter_b_reach"]
    df["sig_str_diff"] = df["fighter_a_sig_str"] - df["fighter_b_sig_str"]

    # 0.1 features
    df["reach_height_ratio_diff"] = (
        ( (df["fighter_a_reach"] + 1) / (df["fighter_a_height"] + 1) ) -
        ( (df["fighter_b_reach"] + 1) / (df["fighter_b_height"] + 1) )
    )
    df["finish_rate_diff"] = (
        ( (df["fighter_a_finishes"] + 1) / (df["fighter_a_total_wins"] + 1) ) -
        ( (df["fighter_b_finishes"] + 1) / (df["fighter_b_total_wins"] + 1) )
    )
    df["wl_ratio_diff"] = (
            ( (df["fighter_a_total_wins"] + 1) / (df["fighter_a_total_losses"] + 1)) -
            ( (df["fighter_b_total_wins"] + 1) / (df["fighter_b_total_losses"] + 1))
    )
    df["5_round_exp_diff"] = df["fighter_a_5_round_fights"] - df["fighter_b_5_round_fights"]
    df["fight_time_diff"] = df["fighter_a_total_fight_time"] - df["fighter_b_total_fight_time"]
    df["td_attempt_diff"] = df["fighter_a_avg_td_attempts"] - df["fighter_b_avg_td_attempts"]

    # 0.2 features
    # Rank difference (Champ = 0, Unranked = 999)
    df["rank_diff"] = df["fighter_a_rank"].fillna(999) - df["fighter_b_rank"].fillna(999)
    # Last 4 fight win difference
    df["last_4_win_diff"] = df["fighter_a_last_4_wins"] - df["fighter_b_last_4_wins"]
    # Last 4 finish difference (KO/TKO/Submission)
    df["last_4_finish_diff"] = df["fighter_a_last_4_finishes"] - df["fighter_b_last_4_finishes"]
    # Current win streak difference
    df["win_streak_diff"] = df["fighter_a_win_streak"] - df["fighter_b_win_streak"]


    return df

def add_label_column(df):

    # Add's a 'winner' label: 1 if Fighter A wins, 0 otherwise

    df["winner"] = (df["winner_name"] == df["fighter_a_name"]).astype(int)
    return df
