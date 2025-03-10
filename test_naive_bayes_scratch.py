# test_naive_bayes_scratch.py
import numpy as np
from naive_bayes_scratch import NaiveBayesScratch

def test_naive_bayes_scratch():
    X = np.array([[1, 2], [2, 3], [3, 4], [10, 11], [11, 12], [12, 13]])
    y = np.array([0, 0, 0, 1, 1, 1])
    nb = NaiveBayesScratch()
    nb.fit(X, y)
    predictions = nb.predict(X)
    assert (predictions == y).all(), "NaiveBayesScratch predictions are incorrect."
    print("test_naive_bayes_scratch passed.")

if __name__ == "__main__":
    test_naive_bayes_scratch()
