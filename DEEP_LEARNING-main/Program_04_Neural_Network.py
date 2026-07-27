from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris

data = load_iris()
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=100)
model.fit(data.data, data.target)

print("Training Complete")
