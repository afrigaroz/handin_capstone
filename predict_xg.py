import argparse
from src import data_loader, data_validation, preprocessing, features, model, inference

def main(args):
    # Step 1: Load Data
    shots_df = data_loader.load_shots(args.shots_path)
    
    # Step 2: Validate Data
    data_validation.validate_shots_schema(shots_df)
    
    # Step 3: Preprocessing
    shots_df = preprocessing.clean_shots(shots_df)
    
    # Step 4: Feature Engineering
    X, y = features.extract_features(shots_df)
    
    # Step 5: Train and Save Model
    model_path = "models/dummy_model.pkl"
    model.train_and_save_model(X, y, model_path)
    
    # Step 6: Inference and Save Predictions
    inference.run_inference(X, model_path, args.output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--shots_path", required=True)
    parser.add_argument("--tracking_path", required=False)  # Not used in dummy
    parser.add_argument("--output_path", required=True)
    args = parser.parse_args()
    main(args)
