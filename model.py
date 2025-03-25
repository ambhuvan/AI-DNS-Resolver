import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    data = pd.read_csv("dns_logs.csv")
    X = data.drop("label", axis=1)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "dns_model.pkl")

def ai_resolve(domain):
    model = joblib.load("dns_model.pkl")
    features = [1, 10, 0.5]  # Dummy features
    prediction = model.predict([features])[0]
    return "Blocked: Malicious Domain" if prediction == 1 else "Safe: " + domain

if __name__ == "__main__":
    train_model()
