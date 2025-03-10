# test_simple_nn.py
import numpy as np
from simple_nn import SimpleNeuralNetwork

def test_simple_neural_network():
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    Y = np.array([[0], [1], [1], [0]])
    nn = SimpleNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    nn.train(X, Y, epochs=1000, learning_rate=0.1)
    predictions = nn.predict(X)
    assert all(p in [0, 1] for p in predictions.flatten()), "Predictions must be binary."
    print("test_simple_neural_network passed.")

if __name__ == "__main__":
    test_simple_neural_network()
