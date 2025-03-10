# test_logistic_regression_scratch.py
import numpy as np
from logistic_regression_scratch import LogisticRegressionScratch

def test_logistic_regression_scratch():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])
    model = LogisticRegressionScratch(learning_rate=0.1, n_iters=1000)
    model.fit(X, y)
    predictions = model.predict(X)
    assert (predictions == y).all(), "Binary predictions do not match expected labels."
    print("test_logistic_regression_scratch passed.")

if __name__ == "__main__":
    test_logistic_regression_scratch()
