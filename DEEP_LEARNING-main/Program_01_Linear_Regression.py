import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([1,2,3,4,5])
Y = np.array([2,4,6,8,10])

w, b = 0, 0
lr = 0.01
losses = []

for i in range(100):
    y_pred = w*X + b
    loss = np.mean((Y - y_pred)**2)
    losses.append(loss)

    dw = -2*np.mean(X*(Y - y_pred))
    db = -2*np.mean(Y - y_pred)

    w -= lr*dw
    b -= lr*db

plt.plot(losses)
plt.title("Loss Curve")
plt.show()
First program
