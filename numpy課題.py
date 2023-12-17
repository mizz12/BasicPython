#問１ ndarrayの生成

import matplotlib.pyplot as plt
import BasicPython.numpy課題 as np

np.random.seed(0)

x = np.linspace(0,5,100) #観測値 x: 初項0，末項5，項数100の等差数列

noise = np.random.normal(0, 1, 100) #ノイズ noise: 標準正規分布に従う100個の乱数

def y(x):
    """真の関数"""
    return 3 - 5 * x + x ** 2  #真の関数 y(x) = 3 - 5x + x^2の定義



#問2 ndarrayの操作

t = y(x) + noise #観測値xに対応する目標値t

plt.scatter(x,t) #matplotlib で可視化



#問3 ndarrayの結合

x0 = np.ones_like(x) #x0: 長さが x と同じで要素が全て1のndarray
x1 = x               #x1: 観測値 x の各要素を1乗したndarray
x2 = x ** 2          #x2: 観測値 x の各要素を2乗したndarray

X = (np.vstack((x0,x1,x2))).T #垂直方向に結合した2次元配列を転置した行列 X



#問4  線形代数

w0, w1, w2 = (np.linalg.inv((X.T @ X))) @ (X.T) @ t #パラメータのベクトル 
pred_y = w0 + w1 * x + w2 * x ** 2 #観測値 x, t をもとに真の関数 y を2次関数で回帰

plt.scatter(x, t) #先ほどのグラフに真の関数(緑)と回帰曲線(赤)を重ねる
plt.plot(x, pred_y, linewidth=5, color="red", label="pred")
plt.plot(x, y(x), linewidth=5, color="green", label="true")
plt.legend()