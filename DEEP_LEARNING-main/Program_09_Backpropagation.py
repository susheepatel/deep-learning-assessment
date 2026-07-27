w = 0.5
x = 2
y_true = 4

y_pred = w*x
loss = (y_true - y_pred)**2

grad = -2*x*(y_true - y_pred)
w = w - 0.01*grad

print("Updated weight:", w)
