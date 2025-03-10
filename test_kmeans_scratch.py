# test_kmeans_scratch.py
import numpy as np
from kmeans_scratch import KMeansScratch

def test_kmeans_scratch():
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])
    kmeans = KMeansScratch(n_clusters=2, n_iters=100)
    kmeans.fit(X)
    labels = kmeans.predict(X)
    assert len(np.unique(labels)) == 2, "Expected 2 clusters."
    print("test_kmeans_scratch passed.")

if __name__ == "__main__":
    test_kmeans_scratch()
