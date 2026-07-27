import numpy as np

data = np.random.normal(5, 2, 1000)

mu = np.mean(data)
var = np.var(data)

print("Estimated Mean:", mu)
print("Estimated Variance:", var)
