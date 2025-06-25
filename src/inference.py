import pandas as pd
import joblib

def run_inference(X, model_path, output_path):
    clf = joblib.load(model_path)
    preds = clf.predict(X)
    out_df = X.copy()
    out_df['prediction'] = preds
    out_df.to_csv(output_path, index=False)
