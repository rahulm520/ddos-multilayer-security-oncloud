import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simulated data
np.random.seed(42)
data = {
    'packet_rate': np.random.randint(10, 1000, 500),
    'connection_count': np.random.randint(1, 200, 500),
    'ip_entropy': np.random.rand(500)
}
df = pd.DataFrame(data)
df['is_attack'] = (df['packet_rate'] > 600) | (df['connection_count'] > 100)

X = df[['packet_rate', 'connection_count', 'ip_entropy']]
y = df['is_attack'].astype(int)

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved as model.pkl")
