# linear_regression_scratch.py
import numpy as np

class LinearRegressionScratch:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        
    def fit(self, X, y):
        """
        Fit the linear regression model using the normal equation.
        
        Args:
            X (numpy.ndarray): Input features of shape (n_samples, n_features).
            y (numpy.ndarray): Target values of shape (n_samples,).
        """
        X_bias = np.c_[np.ones(X.shape[0]), X]
        theta = np.linalg.inv(X_bias.T.dot(X_bias)).dot(X_bias.T).dot(y)
        self.intercept_ = theta[0]
        self.coef_ = theta[1:]
        
    def predict(self, X):
        """
        Predict target values for given input data.
        """
        return self.intercept_ + X.dot(self.coef_)

if __name__ == "__main__":
    X = np.array([[1], [2], [3], [4]])
    y = np.array([3, 5, 7, 9])
    model = LinearRegressionScratch()
    model.fit(X, y)
    predictions = model.predict(X)
    print("Predictions:", predictions)
