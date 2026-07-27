import numpy as np

X = np.array([1,2,3])
Y = np.array([2,4,6])

w = 0
lr = 0.01

for i in range(10):
    for j in range(len(X)):
        y_pred = w*X[j]
        grad = -2*X[j]*(Y[j]-y_pred)
        w -= lr*grad

print("Weight:", w)
