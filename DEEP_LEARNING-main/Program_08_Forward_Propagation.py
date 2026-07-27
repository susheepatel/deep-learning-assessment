import numpy as np

X = np.array([1,2])
W = np.array([[0.5,0.2],[0.3,0.7]])

Z = np.dot(X,W)
A = 1/(1+np.exp(-Z))

print("Output:", A)
