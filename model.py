import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("dataset.csv")

model = IsolationForest(contamination=0.2)
model.fit(data)


def detect(requests, failed):

    risk_score = int(((requests/150)*50) + ((failed/20)*50))

    if risk_score > 100:
        risk_score = 100

    if requests > 150 or failed > 20:
        result = "⚠ Anomaly Traffic Detected (Possible DDoS Attack)"
        level = "HIGH"

    elif requests > 100 or failed > 10:
        result = "⚠ Suspicious Traffic Detected"
        level = "MEDIUM"

    else:
        result = "✅ Normal Traffic"
        level = "LOW"

    return result, risk_score, level