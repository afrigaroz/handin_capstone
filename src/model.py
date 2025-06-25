from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model(X, y, model_path):
    clf = LogisticRegression()
    clf.fit(X, y)
    joblib.dump(clf, model_path)
