# kmeans_scratch.py
import numpy as np

class KMeansScratch:
    def __init__(self, n_clusters=2, n_iters=100):
        self.n_clusters = n_clusters
        self.n_iters = n_iters
        self.centroids = None
        
    def fit(self, X):
        n_samples, _ = X.shape
        random_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_indices]
        
        for _ in range(self.n_iters):
            clusters = self._create_clusters(X)
            new_centroids = np.array([X[clusters == i].mean(axis=0) if len(X[clusters == i]) > 0 
                                       else self.centroids[i] for i in range(self.n_clusters)])
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
    
    def _create_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
    
    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

if __name__ == "__main__":
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    kmeans = KMeansScratch(n_clusters=2, n_iters=100)
    kmeans.fit(X)
    labels = kmeans.predict(X)
    print("Cluster labels:", labels)
