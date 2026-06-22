
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# for Q4
def rating_group(rating):
    if rating < 1200:
        return 'Beginner'
    elif rating < 1500:
        return 'Intermediate'
    elif rating < 1800:
        return 'Advanced'
    else:
        return 'Expert'

# for Q4
def get_winner_group(row):
    if row['winner'] == 'White':
        return row['white_group']
    elif row['winner'] == 'Black':
        return row['black_group']
    else:
        return 'Draw'

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
    numeric_cols = ['turns', 'white_rating', 'black_rating', 'rating_diff']
    chess_games_df['time_control'] = chess_games_df['time_increment'].str.split('+').str[0].astype(float)
    numeric_cols.append('time_control')
    correlation_matrix = chess_games_df[numeric_cols].corr()
    print(f"correlation_matrix round 3=> : {correlation_matrix.round(3)}")
    # draw correlation_matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix,
                annot=True,
                cmap='coolwarm',
                center=0,
                square=True,
                fmt='.3f')
    plt.title('Correlation Matrix of Chess Game Variables')
    plt.show()
    #
    print("Question 3 is finished")

def q4():
    print("Question 4 is started")
    chess_games_df['white_group'] = chess_games_df['white_rating'].apply(rating_group)
    chess_games_df['black_group'] = chess_games_df['black_rating'].apply(rating_group)

    chess_games_df['winner_group'] = chess_games_df.apply(get_winner_group, axis=1)
    contingency_table = pd.crosstab(chess_games_df['white_group'], chess_games_df['winner_group'])
    print(f"contingency_table:\n {contingency_table}")

    print("Question 4 is finished")



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

# ########################## Question 4
q4()
