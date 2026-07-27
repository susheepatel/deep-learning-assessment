from sklearn.neural_network import MLPClassifier

model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=500)
model.fit(X,y)

print("MLP Accuracy:", model.score(X,y))
