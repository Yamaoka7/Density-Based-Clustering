from sklearn.cluster import DBSCAN

def detect_anomalies_dbscan(data):
    dbscan = DBSCAN(eps=3, min_samples=2)
    dbscan.fit(data)
    labels = dbscan.labels_
    anomalies = data[labels == -1]
    return anomalies

# Example usage:
data = [[1], [2], [3], [10], [15], [100]]
anomalies = detect_anomalies_dbscan(data)
print("Anomalies:", anomalies)
