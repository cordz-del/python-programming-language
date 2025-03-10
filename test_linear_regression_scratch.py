# test_linear_regression_scratch.py
import numpy as np
from linear_regression_scratch import LinearRegressionScratch

def test_linear_regression_scratch():
    X = np.array([[1], [2], [3], [4]])
    y = np.array([3, 5, 7, 9])
    model = LinearRegressionScratch()
    model.fit(X, y)
    predictions = model.predict(X)
    assert np.allclose(predictions, y, atol=1e-6), "Predictions do not match expected values."
    print("test_linear_regression_scratch passed.")

if __name__ == "__main__":
    test_linear_regression_scratch()
