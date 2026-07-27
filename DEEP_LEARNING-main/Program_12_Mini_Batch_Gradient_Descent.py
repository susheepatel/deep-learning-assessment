import numpy as np

# Input data
X = np.array([1, 2, 3, 4, 5, 6], dtype=float)
Y = np.array([2, 4, 6, 8, 10, 12], dtype=float)

# Initialize weight
w = 0.0

# Batch size
batch_size = 2

# Mini-Batch Gradient Descent
for i in range(0, len(X), batch_size):
    xb = X[i:i + batch_size]
    yb = Y[i:i + batch_size]

    y_pred = w * xb
    grad = -2 * np.mean(xb * (yb - y_pred))
    w = w - 0.01 * grad

print("Weight:", w)
