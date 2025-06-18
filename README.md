<<<<<<< HEAD
# ⚽ Enhanced xG Prediction Pipeline — Driblab Capstone

This repository contains a modular and testable pipeline for predicting **enhanced expected goals (xG)** using football event and tracking data.

Unlike traditional xG models that only consider shot location or body part, this project is designed to incorporate rich context — such as player positions and defensive pressure.

---

## 🎯 Objectives

- Align event (shot) and tracking data using timestamps
- Build a test pipeline that runs end-to-end
- Deliver a structured, professional, and reproducible repo

---

## 🧰 Tech Stack

- **Python 3.8+**
- `pandas` — data handling
- `scikit-learn` — dummy classifier
- `joblib` — saving/loading model
- `json` — parsing `.json` and `.jsonl` files
- `argparse` — command-line interface

---

## 🗂️ Folder Structure
```
enhanced-xg-predictor/
├── shots/ # Shot data (JSON format)
├── jsonls/ # Tracking data (JSONL format)
├── model/
│ └── model.pkl # Dummy model file
├── output/
│ └── 661620_predictions.csv
├── predict_xg.py # Main script that runs the pipeline
├── load_input_data.py # Aligns shot + tracking frames
├── build_dummy_model.py # Creates dummy model for testing
├── requirements.txt # List of required Python libraries
└── README.md # This guide
```

---

## 🚀 How to Run the Project

### 1. Setup Environment

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/handin_capstone.git
cd handin_capstone
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dummy model

```
python build_dummy_model.py
```

### 4. Run the prediction pipeline

```
python predict_xg.py --match_id 661620
```

---
## 👤 Author
```
Martin Gutierrez
Diego Lopez
Alexander Karam
Yotaro Enomoto
Africa Bajils
Alejandro Osto
```
---

## 🛠️ Troubleshooting

| Problem                   | Solution                                              |
|---------------------------|-------------------------------------------------------|
| `model.pkl` not found     | Run `python build_dummy_model.py` first               |
| `shots/*.json` not found  | Ensure the file is inside the `shots/` folder         |
| `jsonls/*.jsonl` not found| Ensure the file is inside the `jsonls/` folder        |
| `predict_xg.py` fails     | Make sure the match_id matches your file names        |

---

