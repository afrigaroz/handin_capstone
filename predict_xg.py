# predict_xg.py

"""
This is the main script that simulates enhanced xG prediction.
It uses dummy data, dummy features, and a dummy model to prove the pipeline works.
"""

import argparse
import os
import pandas as pd
import joblib
from load_input_data import find_input_pair

# -------------------------------------
# Dummy feature extractor
# -------------------------------------
def extract_features(shot, frame):
    """
    Returns 5 simple features as placeholders.
    Replace this later with real tracking-based features.
    """
    shot_x = shot["location"]["x"]
    shot_y = shot["location"]["y"]
    ball_x = frame["ball"][0]
    ball_y = frame["ball"][1]
    right_foot = 1 if shot["shot"]["bodyPart"] == "right_foot" else 0

    return [shot_x, shot_y, ball_x, ball_y, right_foot]

# -------------------------------------
# Main pipeline function
# -------------------------------------
def predict_xg(match_id):
    # Load aligned data
    input_pairs = find_input_pair(
        match_id,
        shots_dir="shots",
        tracking_dir="jsonls"
    )

    # Load dummy model
    model = joblib.load("model/model.pkl")

    results = []

    for shot, frame in input_pairs:
        features = extract_features(shot, frame)
        prob = model.predict_proba([features])[0][1]

        results.append({
            "shot_id": shot["id"],
            "videoTimestamp": shot["videoTimestamp"],
            "enhanced_xg": round(prob, 4),
            "isGoal": shot["shot"]["isGoal"]
        })

    # Save to CSV
    os.makedirs("output", exist_ok=True)
    output_path = f"output/{match_id}_predictions.csv"
    pd.DataFrame(results).to_csv(output_path, index=False)
    print(f"✅ Predictions saved to {output_path}")

# -------------------------------------
# Run via command line
# -------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--match_id", required=True, help="Match ID (e.g. 661620)")
    args = parser.parse_args()

    predict_xg(args.match_id)
