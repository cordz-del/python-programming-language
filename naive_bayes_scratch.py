# naive_bayes_scratch.py
import numpy as np

class NaiveBayesScratch:
    def fit(self, X, y):
        """
        Fit a Naive Bayes classifier.
        
        Args:
            X (numpy.ndarray): Features of shape (n_samples, n_features).
            y (numpy.ndarray): Labels of shape (n_samples,).
        """
        self.classes = np.unique(y)
        n_features = X.shape[1]
        self.mean = {}
        self.var = {}
        self.priors = {}
        
        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = np.mean(X_c, axis=0)
            self.var[c] = np.var(X_c, axis=0)
            self.priors[c] = X_c.shape[0] / X.shape[0]
    
    def predict(self, X):
        """
        Predict class labels for the input samples.
        """
        return np.array([self._predict(x) for x in X])
    
    def _predict(self, x):
        posteriors = []
        for c in self.classes:
            prior = np.log(self.priors[c])
            class_conditional = -0.5 * np.sum(np.log(2 * np.pi * self.var[c])) - 0.5 * np.sum(((x - self.mean[c]) ** 2) / (self.var[c] + 1e-8))
            posterior = prior + class_conditional
            posteriors.append(posterior)
        return self.classes[np.argmax(posteriors)]

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [10, 11], [11, 12], [12, 13]])
    y = np.array([0, 0, 0, 1, 1, 1])
    nb = NaiveBayesScratch()
    nb.fit(X, y)
    predictions = nb.predict(X)
    print("Predictions:", predictions)
