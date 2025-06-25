import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

def extract_features(df):
    df['distance_from_goal'] = np.sqrt(df['location.x']**2 + df['location.y']**2)
    le = LabelEncoder()
    df['bodyPart_encoded'] = le.fit_transform(df['shot.bodyPart'])
    
    X = df[['location.x', 'location.y', 'distance_from_goal', 'bodyPart_encoded']]
    y = df['shot.isGoal'].astype(int)
    return X, y
