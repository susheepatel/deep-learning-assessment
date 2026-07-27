from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification

X,y = make_classification(n_samples=100,n_features=2,n_classes=2,n_redundant=0)

model = Perceptron()
model.fit(X,y)

print("Accuracy:", model.score(X,y))
