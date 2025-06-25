# Enhanced xG Prediction Pipeline — Driblab Capstone 
![Goal Prediction](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJHvLlRKGUnTUaaPsN-l_NwY-NB82qNag83w&s)

This project builds a modular MLOps pipeline to predict whether a football shot results in a goal (`1`) or not (`0`) using XGBoost. The pipeline is structured for scalability and production-readiness.

### Key features:
- End-to-end modular pipeline (data loading → inference)
- Feature engineering on spatial shot data
- Binary classification with XGBoost
- Output saved as CSV for downstream use

### Models used:
- **XGBoostClassifier** (can be replaced with other models)
- Dummy features (distance to goal, body part encoding) → planned to replaced

---

## Setup

#### 1. Clone this repository  
#### 2. Create and activate virtual environment
```bash
conda create -n xg_goal python=3.12 pip
conda activate xg_goal
pip install -r requirements.txt
```

#### 3. Place input data  
```
data/raw/shots/661620.json  
data/raw/tracking/661620_tracking_data.jsonl
```

---

## File Structure
```
├── data/
│   └── raw/
│       ├── shots/
│       └── tracking/
│
├── models/                   # Saved XGBoost model
├── output/                   # Predictions CSV
│
├── src/                      # Modular pipeline components
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_validation.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── models.py
│   └── inference.py
│
├── predict_xg.py             # Pipeline entry point
├── requirements.txt
└── README.md
```

---

## Run the Pipeline

```bash
python predict_xg.py \
  --shots_path data/raw/shots/661620.json \
  --tracking_path data/raw/tracking/661620_tracking_data.jsonl \
  --output_path output/predictions.csv
```

---

## Pipeline Stages

- `data_loader.py` – Load JSON shot data  
- `data_validation.py` – Ensure expected schema  
- `preprocessing.py` – Clean/prepare raw inputs  
- `features.py` – Engineer features (e.g. distance to goal)  
- `models.py` – Train and save XGBoost model  
- `inference.py` – Predict goal or no goal (1/0)

---

## Next Steps

- Add real tracking-based features (ball speed, player position)
- Replace dummy features with real feayures
- Integrate evaluation metrics and logging
- Move configs to `config.yaml`
- Add model versioning and MLflow integration

---

## Collaborators  
```
Martin Gutierrez
Diego Lopez
Alexander Karam
Yotaro Enomoto
Africa Bajils
Alejandro Osto
```