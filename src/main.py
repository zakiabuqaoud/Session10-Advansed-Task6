
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def q1():
    print("Q1 is Started...")
    print("Q1: Descriptive statistics profile of chess turns & rating_diff ?")

    descriptive_stats = chess_games_df[['turns', 'rating_diff']].describe(percentiles=[0.25, 0.5, 0.75])
    print(descriptive_stats)
    print("Q1 is Finished...")

def q2_test_normality(data, name):
    print("Q2 is Started...")
    stat, p = stats.shapiro(data.dropna())
    print(f"{name}: p-value = {p:.4f} → {'Normal' if p > 0.05 else 'Not Normal'}")

def q2_log():
    chess_games_df['log_turns'] = np.log(chess_games_df['turns'])
    chess_games_df['log_rating_diff'] = np.log1p(chess_games_df['rating_diff'])

    # skew
    print(f"Turns: {stats.skew(chess_games_df['turns'].dropna()):.3f} : {stats.skew(chess_games_df['log_turns'].dropna()):.3f}")
    print(
        f"Rating_Diff: {stats.skew(chess_games_df['rating_diff'].dropna()):.3f} : {stats.skew(chess_games_df['log_rating_diff'].dropna()):.3f}")
    print("Q2 is Finished...")

def q3():
    print("Question 3 is started")
    print("Question 3 is finished")
    pass


 #  ############## Start From Here ################

 # Loading Data
chess_games_df = pd.read_csv("../data/raw/chess_games.csv")
players_df = pd.read_csv("../data/raw/player.csv")

chess_games_df['rating_diff'] = abs(chess_games_df['white_rating'] - chess_games_df['black_rating'])

# Start in Question Solution
#  # ########################## Question 1
q1()

#  # ########################## Question 2
q2_test_normality(chess_games_df['turns'], 'Turns')
q2_test_normality(chess_games_df['rating_diff'], 'Rating_Diff')
# log-transform
q2_log()

# ########################## Question 3
q3()