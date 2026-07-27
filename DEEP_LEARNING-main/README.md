# 🧠 MLA0402-Deep Learning Laboratory Programs

A comprehensive collection of **Deep Learning laboratory experiments** implemented in **Python** using **NumPy**, **Scikit-learn**, and **Matplotlib**. This repository demonstrates the practical implementation of core Machine Learning and Deep Learning algorithms through 13 laboratory experiments.

---

# 🛠 Technologies Used

- Python 3
- NumPy
- Scikit-learn
- Matplotlib

---

# 📖 Overview

This repository contains the implementation of **13 Deep Learning laboratory experiments** covering fundamental Machine Learning and Deep Learning concepts such as:

- Linear Regression
- Maximum Likelihood Estimation (MLE)
- Machine Learning Pipeline
- Neural Networks
- Artificial Neurons
- Perceptron
- Multilayer Perceptron (MLP)
- Forward Propagation
- Backpropagation
- Gradient Descent
- Stochastic Gradient Descent (SGD)
- Mini-Batch Gradient Descent
- Curse of Dimensionality

Each program is implemented in Python with clear, well-structured code and sample outputs for better understanding.

---

# 🎯 Objectives

- Understand the fundamentals of Machine Learning and Deep Learning.
- Implement learning algorithms using Python.
- Learn optimization techniques used in neural networks.
- Compare different neural network models.
- Gain hands-on experience with Scikit-learn and NumPy.

---

# 📚 Laboratory Experiments

## Program 01 – Learning Algorithm (Linear Regression)

**Description**

Implements Linear Regression using Gradient Descent and visualizes the learning process.

### Sample Code

```python
X = np.array([1,2,3,4,5])
Y = np.array([2,4,6,8,10])

y_pred = w * X + b
loss = np.mean((Y - y_pred) ** 2)
```

### Sample Output

```
Loss decreases over iterations

Final Equation:
y ≈ 2x
```

---

## Program 02 – Maximum Likelihood Estimation (MLE)

**Description**

Estimates the mean and variance of normally distributed data using Maximum Likelihood Estimation.

**Sample Output**

```
Estimated Mean : 5.02
Estimated Variance : 3.98
```

---

## Program 03 – Machine Learning Pipeline

**Description**

Builds a complete machine learning workflow including data preprocessing, training, testing, and performance evaluation.

**Sample Output**

```
Accuracy : 96.67%
```

---

## Program 04 – Neural Network

**Description**

Implements a simple Multi-Layer Perceptron (MLP) with one hidden layer.

**Sample Output**

```
Training Complete
```

---

## Program 05 – Artificial Neuron

**Description**

Demonstrates Sigmoid and ReLU activation functions.

**Sample Output**

```
Sigmoid : 0.95
ReLU : 3.00
```

---

## Program 06 – Perceptron

**Description**

Implements the Perceptron algorithm for binary classification.

**Sample Output**

```
Accuracy : 100%
```

---

## Program 07 – Multilayer Perceptron (MLP)

**Description**

Compares the performance of an MLP with a single-layer Perceptron.

**Sample Output**

```
MLP Accuracy : 99%
```

---

## Program 08 – Forward Propagation

**Description**

Computes forward propagation using predefined weights and inputs.

**Sample Output**

```
Output

[0.69 0.83]
```

---

## Program 09 – Backpropagation

**Description**

Updates neural network weights using gradient computation.

**Sample Output**

```
Updated Weight

0.62
```

---

## Program 10 – Gradient Descent

**Description**

Optimizes a cost function using Gradient Descent.

**Sample Output**

```
Iteration 1
x = 4.0

Iteration 10
x = 0.53
```

---

## Program 11 – Stochastic Gradient Descent (SGD)

**Description**

Implements SGD for regression and compares convergence.

**Sample Output**

```
Weight

1.98
```

---

## Program 12 – Mini-Batch Gradient Descent

**Description**

Implements Mini-Batch Gradient Descent for efficient model training.

**Sample Output**

```
Batch Size : 2

Weight : 1.99
```

---

## Program 13 – Curse of Dimensionality

**Description**

Analyzes how increasing feature dimensions affects model performance.

**Sample Output**

```
Dimension : 2   Accuracy : 98%
Dimension : 5   Accuracy : 96%
Dimension : 10  Accuracy : 93%
Dimension : 20  Accuracy : 88%
```

---

# 📂 Repository Structure

```
Deep-Learning-Lab/
│
├── Program_01_Linear_Regression.py
├── Program_02_MLE.py
├── Program_03_ML_Pipeline.py
├── Program_04_Neural_Network.py
├── Program_05_Artificial_Neuron.py
├── Program_06_Perceptron.py
├── Program_07_MLP.py
├── Program_08_Forward_Propagation.py
├── Program_09_Backpropagation.py
├── Program_10_Gradient_Descent.py
├── Program_11_SGD.py
├── Program_12_Mini_Batch_GD.py
├── Program_13_Curse_of_Dimensionality.py
│
├── README.md
└── LICENSE
```

---

# 🎓 Learning Outcomes

- Linear Regression using Gradient Descent
- Maximum Likelihood Estimation (MLE)
- Machine Learning Pipeline
- Artificial Neural Networks
- Artificial Neurons
- Perceptron Algorithm
- Multilayer Perceptron (MLP)
- Forward Propagation
- Backpropagation
- Gradient Descent
- Stochastic Gradient Descent
- Mini-Batch Gradient Descent
- Curse of Dimensionality Analysis

---

# 👨‍💻 Author

**BANDLAPALLI BHANUTEJA REDDY**

**B.Tech – Artificial Intelligence and Machine Learning**

**Saveetha School of Engineering**

---

# 📄 License

This repository is created for **educational and academic purposes**. The programs are intended for learning, experimentation, and reference in the field of Machine Learning and Deep Learning.
