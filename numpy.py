#問１
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

x = np.linspace(0,5,100)

noise = np.random.normal(0, 1, 100)

def y(x):
    """真の関数"""
    return 3 - 5 * x + x ** 2




#問2
t = y(x) + noise

plt.scatter(x,t)




#問3
x = np.array([1,2,3])
X = (np.array([
    [np.where(x > 0, 1, 1)],
    [x],
    [x ** 2]])).T
X




#問4
x = np.linspace(0,5,100)
noise = np.random.normal(0, 1, 100)

def y(x):
    """真の関数"""
    return 3 - 5 * x + x ** 2

t = y(x) + noise

X = (np.array([
    np.ones_like(x),
    x,
    x ** 2])).T


w0, w1, w2 = (np.linalg.det(np.dot(X.T, X))) * (X.T) * t
pred_y = w0 + w1 * x + w2 * x ** 2

plt.scatter(x, t)
plt.plot(x, pred_y, linewidth=5, color="red", label="pred")
plt.plot(x, y(x), linewidth=5, color="green", label="true")
plt.legend()





x = np.linspace(0,5,100)
noise = np.random.normal(0, 1, 100)

def y(x):
    """真の関数"""
    return 5 * np.sin(np.pi * x / 5)

t = y(x) + noise

X = (np.array([
    np.ones_like(x),
    x,
    x ** 2])).T


w0, w1, w2 = (np.linalg.det(np.dot(X.T, X))) * (X.T) * t
pred_y = w0 + w1 * x + w2 * x ** 2


plt.scatter(x, t)
plt.plot(x, pred_y, linewidth=5, color="red", label="pred")
plt.plot(x, y(x), linewidth=5, color="green", label="true")
plt.legend()