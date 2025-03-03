import pandas as pd
from sklearn.ensemble import IsolationForest

# Carregar dados da série temporal
data = pd.read_csv('data/time_series_data.csv')

# Treinando o modelo de detecção de anomalias
model = IsolationForest()
model.fit(data)

# Prevendo anomalias
anomalies = model.predict(data)
data['anomaly'] = anomalies

print(data.head())
