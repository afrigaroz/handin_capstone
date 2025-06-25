import pandas as pd
import json

def load_shots(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return pd.json_normalize(data)
