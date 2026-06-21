
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from scipy import stats

def q1():
    print("Q1 is Started...")
    print("Q1: Descriptive statistics profile of chess turns & rating_diff ?")

    descriptive_stats = chess_games_df[['turns', 'rating_diff']].describe(percentiles=[0.25, 0.5, 0.75])
    print(descriptive_stats)
    print("Q1 is Finished...")

def q2():
    print("Q2 is Started...")

    print("Q2 is Finished...")




 #  ############## Start From Here ################

 # Loading Data
chess_games_df = pd.read_csv("../data/raw/chess_games.csv")
players_df = pd.read_csv("../data/raw/player.csv")

chess_games_df['rating_diff'] = abs(chess_games_df['white_rating'] - chess_games_df['black_rating'])

# Start in Question Solution
q1()
q2()

