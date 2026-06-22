import numpy as np
from sklearn.ensemble import IsolationForest

training_data = np.array([
    [10,100,1],
    [12,110,1],
    [15,120,1],
    [11,105,1],
    [13,115,1]
])

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

model.fit(training_data)

def detect_anomaly(requests_count,
                   payload_size,
                   reputation_score):

    features = [[
        requests_count,
        payload_size,
        reputation_score
    ]]

    prediction = model.predict(features)

    return prediction[0] == -1