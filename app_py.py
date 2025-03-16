# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GD1bF0lTePChtOzMXLF4HjNCvhWxa6Fp
"""

import pandas as pd

# Sample Dataset of Cricket Matches (Dummy Data)
data = {
    'Team1': ['India', 'Australia', 'Pakistan', 'India', 'Australia'],
    'Team2': ['Australia', 'India', 'Sri Lanka', 'Pakistan', 'South Africa'],
    'Venue': ['Mumbai', 'Sydney', 'Lahore', 'Delhi', 'Cape Town'],
    'Team1_Score': [300, 275, 240, 290, 310],
    'Team2_Score': [250, 280, 230, 280, 300],
    'Weather': ['Sunny', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy'],
    'Result': ['India', 'Australia', 'Pakistan', 'India', 'South Africa']  # Outcome of match
}

df = pd.DataFrame(data)

# Show dataset
df

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Encoding categorical variables
label_encoder = LabelEncoder()
df['Team1'] = label_encoder.fit_transform(df['Team1'])
df['Team2'] = label_encoder.fit_transform(df['Team2'])
df['Venue'] = label_encoder.fit_transform(df['Venue'])
df['Weather'] = label_encoder.fit_transform(df['Weather'])
df['Result'] = label_encoder.fit_transform(df['Result'])

# Features and target variable
X = df[['Team1', 'Team2', 'Venue', 'Team1_Score', 'Team2_Score', 'Weather']]
y = df['Result']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predicting
y_pred = knn.predict(X_test)

# Model accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy

!pip install streamlit

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# Sample data (make sure 'Result' column exists)
data = {
    'Team1': ['India', 'Australia', 'Pakistan', 'India', 'Australia'],
    'Team2': ['Australia', 'India', 'Sri Lanka', 'Pakistan', 'South Africa'],
    'Venue': ['Mumbai', 'Sydney', 'Lahore', 'Delhi', 'Cape Town'],
    'Team1_Score': [300, 275, 240, 290, 310],
    'Team2_Score': [250, 280, 230, 280, 300],
    'Weather': ['Sunny', 'Cloudy', 'Sunny', 'Rainy', 'Cloudy'],
    'Result': ['India', 'Australia', 'Pakistan', 'India', 'South Africa']  # Ensure this column is present
}

df = pd.DataFrame(data)

# Debugging: Check the columns of the DataFrame
print("Columns in the DataFrame:", df.columns)
print(df.head())  # Check the first few rows to ensure 'Result' is present

# Function to encode categorical features
def encode_data(df, label_encoder=None):
    # Encoding team names, venues, and weather
    le_team1 = label_encoder['Team1'] if label_encoder and 'Team1' in label_encoder else LabelEncoder()
    le_team2 = label_encoder['Team2'] if label_encoder and 'Team2' in label_encoder else LabelEncoder()
    le_venue = label_encoder['Venue'] if label_encoder and 'Venue' in label_encoder else LabelEncoder()
    le_weather = label_encoder['Weather'] if label_encoder and 'Weather' in label_encoder else LabelEncoder()

    df['Team1'] = le_team1.fit_transform(df['Team1']) if label_encoder is None else le_team1.transform(df['Team1'])
    df['Team2'] = le_team2.fit_transform(df['Team2']) if label_encoder is None else le_team2.transform(df['Team2'])
    df['Venue'] = le_venue.fit_transform(df['Venue']) if label_encoder is None else le_venue.transform(df['Venue'])
    df['Weather'] = le_weather.fit_transform(df['Weather']) if label_encoder is None else le_weather.transform(df['Weather'])

    # Check for the 'Result' column before encoding
    if 'Result' in df.columns:
        le_result = LabelEncoder()
        df['Result'] = le_result.fit_transform(df['Result'])
    else:
        print("Available columns: ", df.columns)  # Debugging line
        raise ValueError("Error: 'Result' column is missing in the DataFrame!")

    return df, {'Team1': le_team1, 'Team2': le_team2, 'Venue': le_venue, 'Weather': le_weather, 'Result': le_result}

# Encode the dataset and store label encoders
df_encoded, label_encoders = encode_data(df)

# Features and target variable
X = df_encoded[['Team1', 'Team2', 'Venue', 'Team1_Score', 'Team2_Score', 'Weather']]
y = df_encoded['Result']

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Streamlit UI and other functionalities can go here...