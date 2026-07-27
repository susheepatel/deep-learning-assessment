from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification

for d in [2, 5, 10, 20]:
    X, y = make_classification(
        n_samples=200,
        n_features=d,
        n_informative=2,
        n_redundant=0,
        random_state=42
    )

    model = KNeighborsClassifier()
    model.fit(X, y)

    print("Dim:", d, "Accuracy:", model.score(X, y))
