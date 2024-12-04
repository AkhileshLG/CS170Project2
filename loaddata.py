import numpy as np
from sklearn.preprocessing import MinMaxScaler
def load_dataset(file_path):
    data = np.loadtxt(file_path)
    labels = data[:, 0]
    features = data[:, 1:]
    
    # Normalize the features
    scaler = MinMaxScaler()
    features = scaler.fit_transform(features)

    return features, labels