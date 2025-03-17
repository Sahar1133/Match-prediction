# -*- coding: utf-8 -*-
"""Knn.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XKizHkhBYvqISyQlmzgEN3OW49fSgswN
"""

pip install scikit-learn pandas streamlit

import logging
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

# Suppress specific warnings
logging.getLogger("streamlit").setLevel(logging.ERROR)

# Define the main function for cricket match prediction
def cricket_prediction():
    st.title('Cricket Match Prediction')

    st.sidebar.header("User Inputs")

    # User inputs for match prediction (classification)
    team_1_score = st.sidebar.number_input('Team 1 Score (Runs)', min_value=0, value=250)
    team_2_score = st.sidebar.number_input('Team 2 Score (Runs)', min_value=0, value=230)

    toss_winner = st.sidebar.selectbox("Toss Winner", ("Team 1", "Team 2"))
    batting_first = st.sidebar.selectbox("Batting First", ("Team 1", "Team 2"))
    weather_condition = st.sidebar.selectbox("Weather Condition", ("Good", "Average", "Bad"))

    # Cricket match prediction (win/loss)
    match_data = pd.DataFrame({
        'team_1_score': [team_1_score],
        'team_2_score': [team_2_score],
        'toss_winner': [toss_winner],
        'batting_first': [batting_first],
        'weather_condition': [weather_condition],
    })

    # Dummy match outcome dataset (You can replace this with your actual dataset)
    data = {
        'team_1_score': [240, 220, 250, 200, 270],
        'team_2_score': [230, 200, 240, 180, 260],
        'toss_winner': ['Team 1', 'Team 2', 'Team 1', 'Team 2', 'Team 1'],
        'batting_first': ['Team 1', 'Team 2', 'Team 1', 'Team 2', 'Team 1'],
        'weather_condition': ['Good', 'Average', 'Bad', 'Good', 'Average'],
        'match_outcome': ['Team 1 Wins', 'Team 2 Wins', 'Team 1 Wins', 'Team 2 Wins', 'Team 1 Wins']
    }

    df = pd.DataFrame(data)

    # Encoding categorical data
    df['toss_winner'] = df['toss_winner'].map({'Team 1': 0, 'Team 2': 1})
    df['batting_first'] = df['batting_first'].map({'Team 1': 0, 'Team 2': 1})
    df['weather_condition'] = df['weather_condition'].map({'Good': 0, 'Average': 1, 'Bad': 2})
    df['match_outcome'] = df['match_outcome'].map({'Team 1 Wins': 0, 'Team 2 Wins': 1})

    # Splitting dataset into features and labels
    X = df.drop('match_outcome', axis=1)
    y = df['match_outcome']

    # Train a KNN classifier for match win prediction
    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X, y)

    # Encode user inputs
    input_data = pd.DataFrame({
        'team_1_score': [team_1_score],
        'team_2_score': [team_2_score],
        'toss_winner': [0 if toss_winner == "Team 1" else 1],
        'batting_first': [0 if batting_first == "Team 1" else 1],
        'weather_condition': [0 if weather_condition == "Good" else (1 if weather_condition == "Average" else 2)],
    })

    # Predict match outcome
    match_prediction = knn_classifier.predict(input_data)
    outcome = "Team 1 Wins" if match_prediction[0] == 0 else "Team 2 Wins"
    st.write(f"Predicted Match Outcome: {outcome}")

    # Score Prediction (regression)
    st.sidebar.header("Score Prediction")

    # Sample data for score prediction (replace with your dataset)
    score_data = {
        'team_1_score': [240, 220, 250, 200, 270],
        'team_2_score': [230, 200, 240, 180, 260],
        'toss_winner': [0, 1, 0, 1, 0],  # Team 1 = 0, Team 2 = 1
        'batting_first': [0, 1, 0, 1, 0],  # Team 1 = 0, Team 2 = 1
        'weather_condition': [0, 1, 2, 0, 1]  # Good = 0, Average = 1, Bad = 2
    }

    score_df = pd.DataFrame(score_data)

    # Predict the total score using KNN Regression
    knn_regressor = KNeighborsRegressor(n_neighbors=3)
    knn_regressor.fit(score_df.drop('team_2_score', axis=1), score_df['team_2_score'])

    # Predict score for the user input
    score_prediction = knn_regressor.predict(input_data.drop('team_2_score', axis=1))
    st.write(f"Predicted Score for Team 2: {score_prediction[0]:.2f} runs")

# Run the cricket match prediction function
if __name__ == "__main__":
    cricket_prediction()



